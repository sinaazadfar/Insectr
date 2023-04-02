from django.db import models

class Child(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/',default='images/blank.png')

    def __str__(self):
        return self.name

class LayerThree(models.Model):
    name = models.CharField(max_length=100)
    children = models.ManyToManyField(Child)

    def __str__(self):
        return self.name
    
class LayerTwo(models.Model):
    name = models.CharField(max_length=100)
    children = models.ManyToManyField(LayerThree)

    def __str__(self):
        return self.name

class LayerOne(models.Model):
    name = models.CharField(max_length=100)
    children = models.ManyToManyField(LayerTwo)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    children = models.ManyToManyField(LayerOne)

    def __str__(self):
        return self.name
    
class Arthropod(models.Model):
    name = models.CharField(max_length=100)
    children = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
