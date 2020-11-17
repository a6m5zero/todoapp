from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    birthdate = models.DateField(blank=True, null=True)
    trello_hash = models.CharField(max_length = 128, default = '', blank=True)
    # avatar = models.ImageField(upload_to="user_avatars/%Y/%m/%d", blank=True, null=True)

    def __str__(self):
        return "Профиль пользователя %s" % self.user.username
    


# Create your models here.
