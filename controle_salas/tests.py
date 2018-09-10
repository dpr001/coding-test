from django.test import TestCase
from controle_salas.models import Agenda

# Create your tests here.


class AgendaTest(TestCase):
    fixtures = ['data.json']

    def test_periodo_invalido_true(self):
        agenda = Agenda()
        result = agenda.periodo_disponivel(
                    {
                        "hora_inicial": "08:00:00",
                        "hora_final": "10:00:00",
                        "data": "2018-09-11",
                        "sala": 1
                    }
                 );

        self.assertTrue(result)


    def test_periodo_invalido_false(self):
        agenda = Agenda()
        result = agenda.periodo_disponivel(
                    {
                        "hora_inicial": "11:00:00",
                        "hora_final": "12:00:00",
                        "data": "2018-09-11",
                        "sala": 1
                    }
                 );

        self.assertFalse(result)


class ControleSalaApiTest(TestCase):

    fixtures = ['data.json']

    def test_post_periodo_invalido(self):

        data = {
                "id": 9,
                "sala": 1,
                "data": "2018-09-11",
                "hora_inicial": "08:00:00",
                "hora_final": "10:00:00"
                }

        response = self.client.post('/api/v1/agenda/', data);

        self.assertEquals(response.status_code, 400)

    def test_post_periodo_valido(self):

        data = {
            "sala": 1,
            "data": "2018-09-12",
            "hora_inicial": "17:00:00",
            "hora_final": "18:00:00"
        }

        response = self.client.post('/api/v1/agenda/', data);

        self.assertEquals(response.status_code, 201)