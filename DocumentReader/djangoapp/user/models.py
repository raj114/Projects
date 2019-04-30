from django.db import models

# Create your models here.
class AppUsers(models.Model):
    name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=30)
    user_password = models.CharField(max_length=30)
    user_mobilenumber = models.CharField(max_length=10)
    user_position = models.CharField(max_length=15)

        
    def __str__(self):
        return self.user_name


class EncodedData(models.Model):
    user_name = models.CharField(max_length=30)
    encoded_text = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user_name
        
class ScanData(models.Model):
    encoded_text = models.CharField(max_length=50)
    user_position = models.CharField(max_length=20)
        
    def __str__(self):
        return self.user_position
