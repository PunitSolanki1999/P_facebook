from django.shortcuts import render,redirect
from .forms import User_signup_form,User_login,User_searching,Update_info,Update_profile
from .models import User_signup

from django.db.models import Q
# Create your views here.

def user_registration(request,*args,**kwargs):
    form = User_signup_form(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit = False)
            if 'profile_pic' in request.FILES:
                instance.picture = request.FILES['profile_pic']
            
            form.save()
            return redirect('user:interface')

    context = {'form':form}
    return render(request,'user/user_registration.html',context)


def user_login(request,*args,**kwargs):
    form = User_login(request.POST or None)
    username_not_available = False
    password_not_available = False
    if request.method == 'POST':
        
        data = request.POST.copy()
        username = data.get('username')
        password = data.get('password')
        print(password)

        try:
            user = User_signup.objects.get(username = username)
            print(user.password)
            if user.username == username and user.password == password:
                request.session['username'] = username
                return redirect('user:user-info')
            else:
                password_not_available = True
        except Exception:
            username_not_available = True

    context = {
        'form': form,
        'username_not_available': username_not_available,
        'password_not_available': password_not_available,
    }

    return render(request,'user/user_login.html',context)
def user_info(request,*args,**kwargs):
    if request.session.has_key('username'):
        username = request.session['username']

        try:
            user = User_signup.objects.get(username =username)
        except Exception:
            return redirect("user:login")


        context = {
            'user': user
        }

        return render(request,'user/user_info.html',context)
    else:
        return redirect('user:login')


def searching(request,*args,**kwargs):
    if request.session.has_key('username'):
        username = request.session['username']
        form = User_searching(request.POST or None)
        user = None
        if request.method == 'POST':
            data = request.POST.copy()
            name = data.get('name')
            if (' ' in name) == True:
                name = name.split(' ')
                print(name)
                print(name[0])
                fname = name[0]
                lname = name[1]
                user = User_signup.objects.filter(Q(fname__contains = fname) & Q(lname__contains = lname))
            else:
                fname = name 
                lname = ' '
                user = User_signup.objects.filter(Q(fname__contains = fname))

        context = {
            'user': user,
            'form': form,
        }
        return render(request,'user/search.html',context)
    else:
        return redirect('user:login')


def user_info_update(request,*args,**kwargs):
    if request.session.has_key('username'):
        username = request.session['username']

        try:
            user = User_signup.objects.get(username =username)
        except Exception:
            pass
        form = Update_info(request.POST or None)
        form.fields['fname'].initial = user.fname
        form.fields['dob'].initial = user.dob
        form.fields['lname'].initial = user.lname
        form.fields['address'].initial = user.address
        form.fields['city'].initial = user.city
        if request.method == 'POST':
            if form.is_valid():
                instance = form.save(commit = False)
                user.fname = instance.fname
                user.lname = instance.lname
                user.dob = instance.dob
                user.address = instance.address
                user.city = instance.city
                user.save()
                return redirect('user:user-info')
        context = {
            'form': form,
            'user': user,
        }
        return render(request,'user/update.html',context)
    else:
        return redirect("user:login")


def logout(request,*args,**kwargs):
    if request.session.has_key('username'):
        if request.method == 'POST':
            data = request.POST.copy()
            if data.get('Yes'):
                log = 'Yes'
                del request.session['username']
                return redirect('user:login')
            elif data.get('No'):
                log = 'No'
                return redirect('user:user-info')
            print(log)
            
           

    return render(request,'user/logout.html')


def search_info(request,pk,*args,**kwargs):
    if request.session.has_key('username'):
        user = User_signup.objects.get(pk=pk)
        context = {
            'user': user,
        }
        return render(request,'user/search_info.html',context)
    else:
        return redirect('user:login')

def update_profile_pic(request,*args,**kwargs):
    if request.session.has_key('username'):
        username = request.session['username']

        try:
            user = User_signup.objects.get(username =username)
        except Exception:
            pass
        form = Update_profile(request.POST or None, request.FILES or None)
        form.fields['picture'].initial = user.picture
        
        if request.method == 'POST':
            if form.is_valid():
                data = request.POST.copy()
                
                if data.get('submit'):
                    instance = form.save(commit = False)
                    if 'profile_pic' in request.FILES:
                        instance.picture = request.FILES['profile_pic']
                    user.picture = instance.picture
                    
                    user.save()
                    return redirect('user:user-info')
                elif data.get('cancel'):
                    return redirect('user:user-info')
        context = {
            'form': form,
            'user': user,
        }
        return render(request,'user/update_profile.html',context)
    else:
        return redirect("user:login")

def interface(request):
    return render(request,'user/interface.html')