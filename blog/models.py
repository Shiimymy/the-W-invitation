from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Memories(models.Model):
    image = models.ImageField(upload_to='media/image', default='placeholder')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="memories_posts"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.author} memory:{self.content}"

