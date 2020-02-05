from django.db import models
from multiselectfield import MultiSelectField

class Request(models.Model):
    SKILL_CHOICES=[
        ('Java','Java'),
        ('C++','C++'),
        ('C','C'),
        ('Python','Python')
    ]
    skills=MultiSelectField(choices=SKILL_CHOICES)
    experience=models.IntegerField()
    notice_period=models.PositiveIntegerField()
    location=models.CharField(max_length=100)
    max_salary=models.FloatField()
    negotiable=models.BooleanField(default=False)
    