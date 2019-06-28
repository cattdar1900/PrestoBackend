from django.db import models

STATES = (
    ('0' , 'off'),
    ('1' , 'on')
)

class callService(models.Model):
    name = models.CharField(max_length= 50)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    status = models.CharField(max_length = 50,choices = STATES)


