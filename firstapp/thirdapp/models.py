from django.db import models

class Employee(models.Model):
    eno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=100) 
    esal = models.FloatField()

    def __str__(self):
        return self.ename
    

class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=20)
    realname = models.CharField(max_length=30)
    
    def __str__(self):
        return self.username