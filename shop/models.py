from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cards(models.Model):
    name = models.CharField(max_length=250)
    sets = models.CharField(max_length=250)
    
    def __str__ (self):
        return self.name + ' - ' + self.sets
        