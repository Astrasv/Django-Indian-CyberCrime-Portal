from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Dont forget to register the models in blogApp.admin.py. Only then we will have the Posts in Django Admin GUI
class Post(models.Model):
    #Learn about auto_date and auto_date now
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # Do NOT use () for now()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #Displays the title of the object while querying using django shell
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # reverse return url as string, but redirect directly redirect us
        # reverses to post-detail url with pk as the current created pk
        return reverse("post-detail", kwargs={"pk": self.pk}) 
    


# Django shell query notes

# First import the classes from the blogApp
# Use Class.objects.all() to get a queryset of all objetcs of the class
# Use Post.objects.first() to get an output of an Post object (NOT a query set)
# user = User.objects.filter(username = 'astra').first()
# Access user attributes using .

# post_1 = Post(title = "..", content = "..",author = user)
# post_1.save() used to save it to the DB

# Let use say we need to get the posts done by all the a specific use. We can use _set to get it
# baseobject.relatedModelName_set.all() will fetch all the data in realtedModel with baseobject refered in it
# user.post_set.all()

# We can create a post from a user using .create() 
# user.post_set.create(.... need not mention author because we are already inside a user object)
