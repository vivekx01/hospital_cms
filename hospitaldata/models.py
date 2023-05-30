from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_description = models.TextField()
    dept_contact = models.CharField(max_length=100)
    dept_head_name = models.CharField(max_length=100)
    services = models.ManyToManyField('Service')

    def __str__(self):
        return self.dept_name

class Service(models.Model):
    service_name = models.CharField(max_length=100)

    def __str__(self):
        return self.service_name

class Staff(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    qualifications = models.CharField(max_length=200)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name