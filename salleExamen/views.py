from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny



# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Matiere, Salle, Planification, Examen, User
from .serializers import SalleExamenSerializer, UpdateSalleSerializer, DeleteSalleSerializer, MatiereSerializer,CreateMatiereSerializer

from django.http.response import JsonResponse

from rest_framework import serializers
from rest_framework import status
from salleExamen.models import Matiere
from django.shortcuts import get_object_or_404

from rest_framework_swagger.views import get_swagger_view



class SalleCreateView(generics.CreateAPIView):
    queryset = Salle.objects.all()
    serializer_class = SalleExamenSerializer
    
    

class UpdateSalleView(APIView):
    serializer_class = UpdateSalleSerializer
    
    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        id_salle = serializer.data.get("id_salle")
        nom_salle = serializer.data.get("nom_salle")
        capacite_salle = serializer.data.get("capacite_salle")
        location_salle = serializer.data.get("location")
        disponibilite_salle = serializer.data.get("disponibilite")
        
        salle = Salle.objects.get(id=id_salle)
        if nom_salle:
            salle.nomSalle = nom_salle
            
        if capacite_salle:
            salle.capacite = capacite_salle
            
        if location_salle:
            salle.localisation = location_salle
            
            
        if disponibilite_salle:
            salle.disponibilite = disponibilite_salle
            
            
        salle.save()
        
        return Response(
            data=SalleExamenSerializer(
                Salle.objects.get(id=id_salle)
            ).data
            )

        
class CreateMatiereView(APIView):
    serializer_class = CreateMatiereSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        nom = serializer.data.get("nom")
        description = serializer.data.get("description")
        enseignant_id = serializer.data.get("enseignant_id")
        enseignant = User.objects.get(id=enseignant_id)
        
        matiere:Matiere = Matiere.objects.create(nom=nom, description= description, enseignant=enseignant)
        
        return Response(
            data=MatiereSerializer(
                matiere
            ).data
            )
        

class DeleteSalleView(APIView):
    serializer_class = DeleteSalleSerializer
    
    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        id_salle = serializer.data.get("id_salle")
        try:
            salle = Salle.objects.get(id=id_salle)
            salle.delete()
            return Response(status=200, data="OK")

        except:
            return Response(status=404,data={"erreur":"salle non existante"})



class GetSallesView(APIView):
    
    def get(self, request, *args, **kwargs):
        salles = Salle.objects.all()

        return Response(status=200, data=SalleExamenSerializer(salles, many = True).data)

        
        



schema_view = get_swagger_view(title='Pastebin API')


        



