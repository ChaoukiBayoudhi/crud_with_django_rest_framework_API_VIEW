from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    birthDate = models.DateField()
    country = models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    tshirtNumber=models.PositiveSmallIntegerField()
    photo=models.ImageField(upload_to='photos/', blank=True,null=True)
    class Meta:
        db_table = "player"
        verbose_name = "Player"
        verbose_name_plural = "Players"
        ordering=['name']
    def __str__(self):
        return self.name