from odoo import models, fields, api, _
from odoo.exceptions import ValidationError



class CReateAPpointment(models.TransientModel):
    _name = 'create.appointment'
    _description = 'Create Appointment'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    appointment_date = fields.Date(string='Appointment Date', required=True)

    def create_appointment(self):
        appointment_id = self.env['hospital.appointment'].create({
            'patient_id': self.patient_id.id,
            'appointment_date': self.appointment_date,
            'notes': 'Created from the wizard',
        })
        self.patient_id.message_post(body='Appointment Created Successfully', subject='Appointment Creation')
        #return to the newly created appointment
        return {
            'name': _('Appointments'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'hospital.appointment',
            'res_id': appointment_id.id,
            'type': 'ir.actions.act_window',
        }

    def get_data(self):
        print("Get Data Method Called from Wizard")
        print("Patient ID: ", self.patient_id.id)
        print("Appointment Date: ", self.appointment_date)
