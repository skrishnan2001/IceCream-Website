from django.db import models
#makemigrations - create migrations and store in a file
#migrate - apply the pending changes created by makemigrations

class Contact(models.Model):
     name = models.CharField(max_length=122)
     email = models.CharField(max_length=122)
     phone = models.CharField(max_length=13)
     desc = models.TextField()
     date = models.DateField()

     def __str__(self):
          return self.name