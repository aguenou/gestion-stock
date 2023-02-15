from django.test import TestCase, Client

# Create your tests here.
class ListMeubleAPIViewsetTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.meubles = [
            {"nom": "Canapé",
             "etat": "OC",
             "prix": 500.0,
             "lieu": 1,
             "statut": "LBR"
            },
            {"nom": "Chaise",
             "etat": "NF",
             "prix": 200.0,
             "lieu": 1,
             "statut": "LBR"
            },
        ]

    def test_meuble_create(self):
        response = self.client.post('/api/meuble/', data=self.meubles)
        self.assertEqual(response.status_code, 201)

    def test_meuble_list(self):
        response = self.client.get('/api/meuble/')
        self.assertEqual(response.status_code, 200)

