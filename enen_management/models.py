from django.db import models

class Catagory(models.Model):
      name=models.CharField(max_length=20)
      description=models.CharField(max_length=500)
class Event(models.Model):
    name = models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    date = models.DateField()
    time=models.TimeField()
    title =models.CharField(max_length=70,default="Untitled")
    location = models.CharField(max_length=200)
    category=models.ForeignKey(Catagory, on_delete=models.CASCADE, null=True, blank=True)


def __str__(self):
        return self.name

class participant(models.Model):
      name=models.CharField(max_length=500)
      email=models.EmailField()
      # event=models.ManyToManyField(Event,on_delete=models.CASCADE,related_name='participant')