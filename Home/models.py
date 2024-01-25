from django.db import models

class Data(models.Model):
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    phoneno = models.IntegerField()
    address = models.CharField(max_length = 1000)

    def __str__(self):
        return self.name 