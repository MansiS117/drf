from django.db import models


# Create your models here.
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    class Meta:
        ordering = ["created"]
