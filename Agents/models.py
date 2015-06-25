from django.db import models

class AgentUser(models.Model):
    email = models.CharField(max_length=55)
    password = models.CharField(max_length=55)

class FaceData(models.Model):
    email = models.CharField(max_length=55)
    DATA_0 = models.CharField()
    DATA_1 = models.CharField()
    DATA_2 = models.CharField()
    DATA_3 = models.CharField()
    DATA_4 = models.CharField()
