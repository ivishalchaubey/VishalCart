from django.db import models
from django.contrib.auth.models import User

class extenduser(models.Model):
	mobile_no = models.CharField(max_length=12)
	dateofbirth = models.CharField(max_length=55)
	user = models.OneToOneField(User,on_delete = models.CASCADE)

