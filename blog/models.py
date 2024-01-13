from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from multiselectfield import MultiSelectField


class Memories(models.Model):
    """
    Model for Memories posts
    """

    LOCATIONS = (
        ('Church', 'Church'),
        ('Town Hall', 'Town Hall'),
        ('Venue', 'Venue'),
        ('Other', 'Other'),
    )
    
    INVITER_OPTION = (
        ('bride', 'Bride'),
        ('groom', 'Groom'),
    )

    image = CloudinaryField('image', default='placeholder', blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="memories_posts"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    approved = models.BooleanField(default=False)
    location = models.CharField(max_length=20, choices=LOCATIONS)
    inviter = MultiSelectField(choices=INVITER_OPTION, max_choices=2, default='Bride')

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.author} memory:{self.content}"
