from django.db import models
from django.contrib.auth.models import User


from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# class Author(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.ImageField(upload_to='profile_pics')

#     def __str__(self):
#         return self.user.username
    
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title
    

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='category')
    featured = models.BooleanField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    # def save_model(self, request, obj, form, change):
    #     # associating the current logged in user to the client_id
    #     obj.author = request.user
    #     super().save_model(request, obj, form, change)