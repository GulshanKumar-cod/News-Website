from django.db import models

# Create your models here.
#makemigrations = create changes and store in a file
#migrate = apply the pending changes created by makemigrations

class Contact(models.Model):
    name  = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    desc  = models.TextField()
    date  = models.DateField()

    def __str__(self):
        return self.name
    ()