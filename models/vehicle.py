from odoo import models, fields, api

class Vehicle(models.Model):
    _name = "vehicle"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Mantenimiento de vehiculos"

    tipo_vehiculo = fields.Selection([
        ('1', 'Sedan'),
        ('2', 'Suv'),
        ('3', 'Camioneta'),
        ('4', 'Minibus'),
        ('5', 'Autobuses'),
    ], string = 'Cantidad de pasajeros', default='other', tracking=True, required = True)
    brand = fields.Char(string = "Marca", required = True)
    car_model = fields.Char(string = "Modelo", required = True)
    year = fields.Date(string = "Año", required = True)
    plate_number = fields.Char(string = "Placa", required = True)
    image = fields.Binary()

    state = fields.Selection([
        ('disponible', 'Disponible'),
        ('reservado', 'Reservado'),
    ], string='Status',default='disponible')
    # , required=True, readonly=True, copy=False, tracking=True, default='disponible')
    
    def button_disponible(self):
        if(self.state=='disponible'):
            self.state = 'reservado'
        else:
            self.state = 'disponible'    
        
    def button_reservado(self):
        self.state = 'reservado'