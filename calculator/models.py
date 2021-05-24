from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class BodyWeight(models.Model):

#     WEIGHT_CHOICES = (

#         ('kilogram','kg'),
#         ('pounds','p'),
#         ()
#     )

#     kilo = models.IntegerField(max_length=3)
#     weight = models.CharField(max_length=50,choices=WEIGHT_CHOICES)


# class BodyHeight(models.Model):

#     HEIGHT_CHOICES = ( 

#         ('feet','ft'),
#         ('inches','in'),
#         ('centimetre','cm')
#     )

#     height = models.CharField(max_length=50,choices=HEIGHT_CHOICES)


class Bmi(models.Model):

    user = models.ForeignKey(User,related_name="bmi",on_delete=models.CASCADE,null=True)
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()

    def __str__(self):
        return self.user.username

    def  bmi(self):
        return self.weight/self.height**2  
         
    #     Convert weight in pounds and height in inches
    #     bmi = weight (lb) / [height (in)]2 x 703

class Suggestion(models.Model):

    BMI_CHOICES = (
        ('underweight','UNDERWEIGHT'),
        ('normalweight','NORMALWEIGHT'),
        ('overweight', 'OVERWEIGHT'),
        ('obsessed','OBSESSEDWEIGHT')
    )
    suggestion = models.CharField(max_length=255,choices=BMI_CHOICES)
    message = models.TextField(max_length=255,null=True)
    
    def __str__(self):
        return self.suggestion
        return self.message
    
