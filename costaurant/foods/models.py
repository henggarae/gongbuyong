from django.db import models
    
    
class menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    img_path = models.CharField(max_length=255)
    price = models.IntegerField()
    def __str__(self):
        return self.name
                                       