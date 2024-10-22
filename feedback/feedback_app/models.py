from django.db import models

# Create your models here.

class FeedbackForm(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    phone_number=models.IntegerField()
    subject=models.CharField(max_length=250)
    questions=models.TextField()

    def __str__(self):
        return f"{self.name},{self.subject}"