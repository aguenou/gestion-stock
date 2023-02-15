from rest_framework.serializers import ModelSerializer
from .models import Dirigeant, Magasin, Meuble


class MeubleSerializer(ModelSerializer):
    class Meta:
        model = Meuble
        fields = ['nom','etat','prix','lieu','statut']


class MagasinSerializer(ModelSerializer):
    lieu = MeubleSerializer(many=True)
    class Meta:
        model = Magasin
        fields = ['nom', 'adresse', 'dirigeant', 'ca']

class DirigeantSerializer(ModelSerializer):
    dirigeant = MagasinSerializer(many=True)

    class Meta:
        model = Dirigeant
        fields = ['nom', 'prenom']


