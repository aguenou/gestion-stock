from rest_framework.response import Response
from .serialisers import DirigeantSerializer, MagasinSerializer, MeubleSerializer
from .models import Dirigeant, Magasin, Meuble
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

class DirigeantAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Dirigeant.objects.all()
        serializer = DirigeantSerializer(categories, many=True)
        return Response(serializer.data)

class MagasinAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Magasin.objects.all()
        serializer = MagasinSerializer(categories, many=True)
        return Response(serializer.data)

class MeubleAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Meuble.objects.all()
        serializer = MeubleSerializer(categories, many=True)
        return Response(serializer.data)

class DirigeantAPIViewset(ModelViewSet):
    serializer_class = DirigeantSerializer
    permission_classes = [IsAdminUser,IsAuthenticated]

    def get_queryset(self):
        
        queryset = Dirigeant.objects.all()
        return queryset


class MeubleAPIViewset(ModelViewSet):
    serializer_class = MeubleSerializer
    permission_classes = [IsAdminUser,IsAuthenticated]

    def get_queryset(self):
        
        queryset = Meuble.objects.all()
        return queryset


class VendreMeubleAPIViewset(ModelViewSet):
    serializer_class = MeubleSerializer
    permission_classes = [IsAdminUser,IsAuthenticated]

    def vendre_meuble(self,meuble_id):
        
        meuble = Meuble.objects.get(id=meuble_id, statut='LBR')
        
        if meuble.statut == 'LBR':
            meuble.statut = 'VDU'
            meuble.lieu.ca += meuble.prix
            meuble.lieu.save()
            meuble.save()
            return meuble


# class AddMeubleAPIViewset(ModelViewSet):
#     serializer_class = MeubleSerializer

#     def post_queryset(self):
#         queryset = Meuble.objects.all()

#         nom = self.request.POST('nom')
#         etat = self.request.POST('etat')
#         lieu = self.request.POST('lieu')
#         prix = self.request.POST('prix')
#         statut = self.request.POST('statut')

#         if nom and statut and lieu and prix is not None:
#             queryset = Meuble.objects.create(nom, etat, prix, lieu, statut)

#             return queryset

# class DeleteMeubleAPIViewset(ModelViewSet):
#     serializer_class = MeubleSerializer

#     def get_queryset(self):

#         meuble = self.request.POST('meuble')

#         if meuble is not None:
#             return Meuble.objects.all().filter(meuble=meuble).delete()

class MagasinAPIViewset(ModelViewSet):
    serializer_class = MagasinSerializer
    permission_classes = [IsAdminUser,IsAuthenticated]

    def get_queryset(self):
        
        queryset = Magasin.objects.all()

        statut = Meuble.objects.values('statut','prix')
        ca = Magasin.objects.values('ca')
        if statut.statut == 'VDU':
            newCa = ca.ca + statut.prix

        return queryset
