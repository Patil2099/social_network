from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import gettext as _
import datetime
from django.utils import timezone
from django.db.models.signals import post_save
from django.utils.safestring import mark_safe

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='London')

class Address(models.Model):
    street_address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.IntegerField(default=0)
    country=models.CharField(max_length=100)
    def __str__(self):
        return self.city
class Profile(models.Model):
    user = models.OneToOneField(User)
    name=models.CharField(max_length=100)
    date_of_birth =  models.DateField(_("Date of Birth"), default=datetime.date.today, null=True, blank=True)
    description = models.CharField(max_length=100, default='')
    city=models.CharField(max_length=100,default='')
    perm_add=models.ForeignKey(Address,on_delete=models.CASCADE)
    #email=models.EmailField(max_length=250,default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)
    gen = (
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    )
    gender=models.CharField(max_length=10,choices=gen)
    def __str__(self):
        self.user

    london = UserProfileManager()

    def __str__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = Profile.objects.create(user=kwargs['instance'])

        post_save.connect(create_profile, sender=User)
    #def url(self):
        
        #if self.externalURL:
         #   return self.externalURL
        #else:
            # is this the best way to do this??
         #   return os.path.join('/',settings.MEDIA_URL, os.path.basename(str(self.image)))

    #def image_tag(self):
       
     #   return mark_safe('<img src="{%' /media/' %}" width="150" height="150" />'.format(self.url()) )
    #image_tag.short_description = 'Image'    

    #def __unicode__(self):
        # add __str__() if using Python 3.x
     #   return self.title
