from django.db import models

# Create your models here.
class your_profile(models.Model):
    name = models.CharField(max_length=40, default=None, unique=True)
    state = models.CharField(max_length=60, default=None)
    city = models.CharField(max_length=60, default=None)
    full_name = models.CharField(max_length=255, default=None)
    title = models.CharField(max_length=50, default=None)
    date_birth = models.CharField(max_length=70,default=None)
    con = models.CharField(max_length=50,default=None)
    phone = models.BigIntegerField(default=None, unique=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
class otp_verify(models.Model):
    name = models.CharField(max_length=40, default=None,unique=True)
    otp = models.CharField(max_length=6, default=None, null=False, unique=True)
    registered_time = models.TimeField(default=None)

    def __str__(self):
        return self.name
    
class image_mod(models.Model):
    image = models.ImageField(upload_to='user_image/%y')

class game_scheduler(models.Model):
    name = models.CharField(max_length=90, default=None)
    email = models.EmailField(max_length=90, default=None)
    phone = models.BigIntegerField(default=None)
    target_name = models.CharField(max_length=90, default=None)
    game = models.CharField(max_length=200, default=None)
    schedule_date = models.DateField(auto_now=False, auto_now_add=False, default=None, max_length=12)
    schedule_time = models.TimeField(default=None, max_length=120)

    def __str__(self):
        return self.target_name
class Contact(models.Model):
    first_name = models.CharField(max_length=60, default=None)
    last_name = models.CharField(max_length=60, default=None)
    email_address = models.EmailField(max_length=255, default=None)
    phone_number = models.BigIntegerField()
    message = models.TextField()

    def __str__(self):
        return self.first_name
