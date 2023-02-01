from django.db import models

# Create your models here.

class Department(models.Model):
    Name=models.CharField(max_length=100, null=False)
    Location=models.CharField(max_length=250)

    def __str__(self):
        return self.Name

class Role(models.Model):
    Name=models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.Name

class Employee(models.Model):
    Firstname=models.CharField(max_length=100, null=False)
    Lastname=models.CharField(max_length=100)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    Salary=models.IntegerField(default=0)
    Bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role, on_delete=models.CASCADE)
    Phone=models.IntegerField(default=0)
    HireDate=models.DateField()

    def __str__(self):
        return "%s %s %s" %(self.Firstname, self.Lastname, self.Phone)

    

