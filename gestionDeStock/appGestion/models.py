from django.db import models

# Create your models here.

class Dirigeant(models.Model):
    nom = models.CharField(max_length=30, unique=True)
    prenom = models.CharField(max_length=30, unique=True)

class Magasin(models.Model):
    nom = models.CharField(max_length=30)
    adresse = models.CharField(max_length=50)
    dirigeant = models.ForeignKey(Dirigeant, related_name='dirigeant', on_delete=models.CASCADE)
    ca = models.FloatField()

class Meuble(models.Model):
    ETAT = [
        ('NF', 'NEUF'),
        ('OC','OCCASION'),
        ('ME','MAUVAIS ETAT'),
        ('INU', 'INUTILSABLE')
    ]
    STATUT = [
        ('LBR', 'LIBRE'),
        ('VDU', 'VENDU')
    ]
    nom = models.CharField(max_length=30)
    etat = models.CharField(max_length=3, choices=ETAT, default="NF")
    prix = models.FloatField()
    statut = models.CharField(max_length=30, choices=STATUT)
    lieu = models.ForeignKey(Magasin, related_name='lieu', on_delete=models.CASCADE)

