from django.db import models

class AgentUser(models.Model):
    email = models.CharField(max_length=55)
    password = models.CharField(max_length=55)

class FaceData(models.Model):
    email = models.CharField(max_length=55)
    DATA_0 = models.ImageField()
    DATA_1 = models.ImageField()
    DATA_2 = models.ImageField()
    DATA_3 = models.ImageField()
    DATA_4 = models.ImageField()
