from django.db import models

# Create your models here.

class Movies(models.Model):
    isim = models.CharField(max_length=255)
    tür = models.CharField(max_length=100)
    yıl = models.DateField()
    aciklama = models.TextField()
    resim = models.ImageField(upload_to ='img/', null=True, blank=True)

    def __str__(self):

        return self.isim
    

    
