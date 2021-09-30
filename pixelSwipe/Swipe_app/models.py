from django.db import models

# Create your models here.


class phoneModel(models.Model):
    Mobile = models.IntegerField(blank=False)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)  # For HOTP Verification
    name = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return str(self.Mobile)

class Profile(models.Model):
    user = models.ForeignKey(phoneModel, related_name="user", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    profile_picture = models.ImageField(null=True,
                                        blank=True,
                                        upload_to='photos',
                                        default='images/user.png',
                                        verbose_name="profile picture"
                                        )


class Like_dislike(models.Model):
    member = models.ForeignKey(phoneModel, related_name="member", on_delete=models.CASCADE)
    user = models.ForeignKey(phoneModel, related_name="users", on_delete=models.CASCADE)
    vote = models.CharField(max_length=50, blank=True)
