from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Salle(models.Model):
    nomSalle = models.CharField(max_length=100)
    capacite = models.IntegerField()
    localisation = models.CharField(max_length=50)
    disponibilite = models.BooleanField()
    
    def __str__(self):
        return self.nomSalle
    
    
    
class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    enseignant = models.ForeignKey(User, related_name="enseignant", on_delete=models.CASCADE)

    
    def __str__(self):
        return self.nom
    
    
    
class Cours(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    duree = models.DurationField()
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE, null=True)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, null=True)


    
    def __str__(self):
        return self.date



class Examen(models.Model):
    nom = models.CharField(max_length=100, blank=False, default = '')
    title = models.CharField(max_length=70, blank=False, default='')
    dateExamen = models.DateField(auto_now_add=True)
    heureExamen = models.DurationField()
    dureExamen = models.DurationField()
    matiere = models.ForeignKey(Matiere, related_name='examens',on_delete=models.CASCADE)
    salles = models.ManyToManyField(Salle)

    
    def __str__(self):
        return self.nom



class Planification(models.Model):
    datedebut = models.DateField()
    datefin = models.DateField()
    cours = models.ForeignKey(Matiere, on_delete=models.CASCADE)    
    def __str__(self):
        return self.cours

  


    


    


