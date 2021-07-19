from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Auteur(models.Model):
    nom = models.CharField(max_length = 200, unique = True)

    def __str__(self):
        return self.nom

class Pub(models.Model):
    reference = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add = True)
    image = models.FileField()
    titre = models.CharField(max_length = 200)
    description = models.TextField()
    auteurs = models.ManyToManyField(Auteur, related_name = 'Pubs', blank = True)
    likeur = models.ManyToManyField(User)

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse("pub_detail", kwargs={"pk": self.pk})
    

class Contacte(models.Model):
    email = models.EmailField(max_length = 100)
    nom = models.CharField(max_length = 200)

    def __str__(self):
        return self.nom


class Demande(models.Model):
    date = models.DateTimeField(auto_now_add = True)
    contacter = models.BooleanField(default = False)
    Contactes=models.ForeignKey(Contacte,on_delete=models.CASCADE)
    #Pub = models.OneToOneField(Pub)

    def __str__(self):
        return self.Contactes.nom


class Videos(models.Model):
    video = EmbedVideoField()

    def get_absolute_url(self):
        return reverse("predications", kwargs={"pk": self.pk})

class Ncontacte(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = CharField(max_length=100)
    messages = models.TextField()

