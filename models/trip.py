from odoo import models, fields, api

class Trip(models.Model):
    _name = "trip"
    _inherit = ['mail.thread','mail.activity.mixin']
    
    destination = fields.Char("Destino", required=True, tracking=True)
    calle = fields.Char("Calle")
    ciudad = fields.Char("Ciudad")
    pais = fields.Many2one('res.country', string="Pais", required=True)
    provincia = fields.Many2one('res.country.state', string="Provincia", required=True)
    description = fields.Char("Motivo", required=True)
    datetime1 = fields.Datetime("Fecha/Hora de salida", required=True, tracking=True)
    datetime2 = fields.Datetime("Fecha/Hora de llegada", required=True, tracking=True)
    pickup_location = fields.Char("Punto de encuentro", required=True, tracking=True)
    department_id = fields.Many2one('hr.department', string="Departamento", required=True)
    driver_id = fields.Many2one('hr.employee', string="Chofer")
    cantidad_pasajeros = fields.Char("Cantidad de pasajeros", required=True)  
    state = fields.Selection(selection=[
        ('draft', 'Borrador'),
        ('enviado', 'Enviado'),
        ('in_progress', 'En Progreso'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
        ('cancel', 'Cancelado'),
    ], string='Status', required=True, readonly=True, copy=False,
    tracking=True, default='draft')
    
    def button_send(self):
       self.write({
           'state': "enviado"
       })
    
    