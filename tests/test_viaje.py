from odoo.tests.common import TransactionCase

class TestVijae(TransactionCase):

    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        self.Trip = self.env["trip"]
        self.trip1 = self.Trip.create({
            "destination": "Los Alcarrizos",
            "calle": "Invi", 
            "ciudad": "Santo Domingo",
            "pais":"Republica Dominicana"})

    def test_viaje_create(self):
        "new viaje are active by default"
        self.asserEquals(
            self.trip1.active, True
        )