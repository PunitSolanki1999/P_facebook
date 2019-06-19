from django.db import models

# Create your models here.
class User_signup(models.Model):
    #STATE_CHOICES = (
    #    (1,"Andra Pradesh"),
    #    (2,"Arunachal Pradesh"),
    #    (3,"Assam"),
    #    (4,"Bihar"),
    #    (5,"Chhattisgarh"),
    #    (6,"Goa"),
    #    (7,"Gujarat"),
    #    (8,"Haryana"),
    #    (9,"Himachal Pradesh"),
    #    (10,"Jammu and Kashmir"),
    #    (11,"Jharkhand"),
    #    (12,"Karnataka"),
    #    (13,"Kerala"),
    #    (14,"Madya Pradesh"),
    #    (15,"Maharashtra"),
    #    (16,"Manipur"),
    #    (17,"Meghalaya"),
    #    (18,"Mizoram"),
    #    (19,"Nagaland"),
    #    (20,"Orissa"),
    #    (21,"Punjab"),
    #    (22,"Rajasthan"),
    #    (23,"Sikkim"),
    #    (24,"Tamil Nadu"),
    #    (25,"Telagana"),
    #    (26,"Tripura"),
    #    (27,"Uttaranchal"),
    #    (28,"Uttar Pradesh"),
    #    (29,"West Bengal"),
#
    #)
    username = models.CharField(max_length=25,unique=True)
    password = models.CharField(max_length=25)
    cpassword = models.CharField(max_length=25)
    picture = models.ImageField(upload_to='profile_pic/',blank=True)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    dob = models.DateField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    #state = models.IntegerField(choices = STATE_CHOICES,default=1)

    def __str__(self):
        return self.username