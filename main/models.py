from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('UserProfile', related_name = 'post')
    recipient = models.ForeignKey('UserProfile', related_name = 'something')
    good = models.TextField(null=True)
    bad = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.author_name

class UserProfile(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    user_id = models.CharField(max_length = 20)
    created = models.DateTimeField(auto_now_add=True)
    new = models.CharField(max_length = 6)
