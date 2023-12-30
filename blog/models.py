from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Memories(models.Model):
    """
    Model for Memories
    """
    LOCATIONS = (
        ('church', 'Church'),
        ('town_hall', 'Town Hall'),
        ('venue', 'Venue'),
    )

    INVITER_OPTION = (
        ('bride', 'Bride'),
        ('groom', 'Groom'),
    )

    image = CloudinaryField('image', default='placeholder')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="memories_posts"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    approved = models.BooleanField(default=False)
    location = models.CharField(
        max_length=20, choices=LOCATIONS, default='Venue')
    people = models.ManyToManyField(User, related_name='other_users')
    inviter = models.CharField(
        max_length=10, choices=INVITER_OPTION, default='Bride')

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.author} memory:{self.content}"
