from odoo import models, fields, api, _
from odoo.exceptions import ValidationError



class CReateAPpointment(models.TransientModel):
    _name = 'create.appointment'
    _description = 'Create Appointment'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    appointment_date = fields.Date(string='Appointment Date')

    def create_appointment(self):
        pass