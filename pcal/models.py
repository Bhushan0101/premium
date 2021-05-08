from django.db import models

# Create your models here.
class Member(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    age = models.IntegerField(max_length=200)


class MemPlan(models.Model):
    COMPONENT_NAMES = [('Si', 'Sum Insured'), ('rt', 'Rate'), ('Tn', 'Tenure')]
    componentName = models.CharField(choices=COMPONENT_NAMES, max_length=200)
    componentValue = models.CharField(max_length=200)
    selectionDateTime = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
