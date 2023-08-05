from django.db import models

# Create your models here.
class actors(models.Model):
    Name = models.CharField(max_length=250)
    Age = models.IntegerField()
    Desc = models.TextField()
    Image = models.ImageField(upload_to="Gallery")

    def __str__(self):
        return self.Name