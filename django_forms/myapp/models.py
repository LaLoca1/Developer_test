from django.db import models

class building_info(models.Model):
    building_id = models.CharField(max_length=20)
    id = models.CharField(primary_key= True, max_length=20) 
    fuel = models.TextField(max_length=20) 
    unit = models.CharField(max_length=3)

    def __str__(self) : 
        return f'{self.id}'


    
