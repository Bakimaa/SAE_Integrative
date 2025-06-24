from django.db import models

class Data(models.Model):
        date = models.DateTimeField(max_length=100)
        heure = models.DateTimeField(max_length = 100)
        capteur_id = models.ForeignKey("capteur_id", on_delete=models.CASCADE, default=None)

        def dico(self):
                return {"date":self.date, "heure":self.heure, "capteur_id":self.capteur_id}


class Capteur(models.Model):
    nom = models.CharField(max_length=100)
    lieu = models.CharField(max_length=100)
    emplacement = models.CharField(max_length=100)

    def dico(self):
        return {"nom": self.nom, "lieu": self.lieu, "emplacement": self.emplacement}
