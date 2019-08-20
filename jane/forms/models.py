from django.db import models

class Jane(models.Model):
    favorite_verse = models.CharField(max_length=50,default="Psalm 33:7")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    animal = models.CharField(max_length=20)
    friend = models.CharField(max_length=20,default="Kevin")
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' likes ' + self.animal + ' and ' + self.favorite_verse
# Create your models here.
