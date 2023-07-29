from django.db import models

class Contact(models.Model) :
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    message=models.TextField()
    phone=models.IntegerField()
    created_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    