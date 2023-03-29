from rest_framework import serializers 
from salleExamen.models import Examen
from salleExamen.models import Salle
from salleExamen.models import Planification
from salleExamen.models import Matiere
from salleExamen.models import User


class SalleExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = (
                  'nomSalle',
                  'id',
                  'capacite',
                  'localisation',
                  'disponibilite',
                  )
        
class PlanificationSerializer(serializers.ModelSerializer): 
    class Meta:
            model = Planification
            fields = ('idPlanification',
                  'datefin',
                  'datedebut',
                  
                  )

class MatiereSerializer(serializers.ModelSerializer): 
    class Meta:
            model = Matiere
            fields = ('idCours',
                  'nomCours',
                  'description',
                  'enseignant',
                  
                  )
class UserSerializer(serializers.ModelSerializer):   
    class Meta:
            model = User
            fields = ('idUser',
                  'nom',
                  'prenom',
                  'adresse',
                  'telephone',
                  
                  )
    

            
class UpdateSalleSerializer(serializers.Serializer):
    id_salle = serializers.IntegerField()
    nom_salle = serializers.CharField(required=False)
    capacite_salle = serializers.IntegerField(required=False)
    location = serializers.CharField(required=False)
    disponibilite = serializers.BooleanField(required=False)
    
    

class UpdateSalleSerializer(serializers.Serializer):
    id_salle = serializers.IntegerField()
    nom_salle = serializers.CharField(required=False)
    capacite_salle = serializers.IntegerField(required=False)
    location = serializers.CharField(required=False)
    disponibilite = serializers.BooleanField(required=False)
    
         
class DeleteSalleSerializer(serializers.Serializer):
    id_salle = serializers.IntegerField()
    
    
class CreateMatiereSerializer(serializers.Serializer):
    nom = serializers.CharField()
    description = serializers.CharField()
    enseignant_id = serializers.IntegerField()
    