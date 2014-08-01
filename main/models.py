from django.db import models

# Create your models here.
# Don't put spaces inbetween your '=' here
class Post(models.Model):
    author = models.ForeignKey('UserProfile', related_name = 'post')
    # Could come up with a better related_name then 'something'
    recipient = models.ForeignKey('UserProfile', related_name = 'something')
    # You may also need to add blank=True here as well
    good = models.TextField(null=True)
    bad = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)


# If you put UserProfile before Post you wouldn't need to put UserProfile in quotes in your Post model
# You should be extended Django's AbstractUser model here and registering this in your settings.py file
# instead of making your own with not all the appropriate fields
class UserProfile(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    user_id = models.CharField(max_length = 20)
    created = models.DateTimeField(auto_now_add=True)
    new = models.CharField(max_length = 6)
    email = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.first_name
