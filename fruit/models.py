from django.db import models

# class Fruit(models.Model):

#     categories = (
#         ("Pome fruits", "Pome fruits"),
#         ("Stone fruits", "Stone fruits"),
#         ("Multiple ftuits", "Multiple ftuits"),
#         ("Nuts ", "Nuts "),
#         ("Small fruits","Small fruits"),
#         )

#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     categori = models.CharField(max_length=15,choices=categories,default="Pome fruits")
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     image = models.ImageField(upload_to='fruits/')
#     available = models.BooleanField(default=True)

    

#     def __str__(self):
#         return self.name