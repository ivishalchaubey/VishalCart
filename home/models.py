from django.db import models

class items(models.Model):
	name = models.CharField(max_length=20)
	description = models.CharField(max_length=55)
	price = models.IntegerField()
	location = models.CharField(max_length=255)
	email = models.EmailField()
	photo = models.ImageField(upload_to='photos/')
	phone = models.BigIntegerField()
	date = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.name

# class upload_model(models.Model):
# 	name = models.CharField(max_length=20)
# 	description = models.CharField(max_length=55)
# 	price = models.IntegerField()
# 	location = models.CharField(max_length=255)
# 	email = models.EmailField()
# 	photo = models.ImageField(upload_to='photos/')
# 	phone = models.BigIntegerField()
# 	date = models.DateTimeField(auto_now=True)


# 	def __str__(self):
# 		return self.name

