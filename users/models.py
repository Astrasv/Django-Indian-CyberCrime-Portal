from django.db import models
from django.contrib.auth.models import User
from PIL import Image



# Make suire to register in admin.py
#Add media root and url in app settings.py
# Whenever we create a user, a profile is created. This is done using signals. refer signals.py

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    
    # When we upload a pfp it gets uploaded to upload_to='profile_pics' directory
    # We have added a media directory in app settings, So its under media/profile_pics
    
    # We need to install PILLOW before using ImageField
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()
        
        img = Image.open(self.image.path) # Opens image of current instance
        if img.height > 300 or img.width>300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Overwrites and save the larger file
            

# user = User.objects.filter(username='astra').first()
# user.profile
# user.profile.image
# user.profile.image.url this is used to get the file path for the html page
# If we did not give any pfp, we have default.jpg in the path