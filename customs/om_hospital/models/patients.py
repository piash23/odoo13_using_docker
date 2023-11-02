from odoo import _, api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = 'Hospital Patient'
    # _rec_name = 'patinet_name'

    patinet_name = fields.Char(string="Patient Name", required=True)
    patinet_age = fields.Integer(string="Age")
    notes = fields.Text(string='Notes')
    image = fields.Binary(string="Image")
    name = fields.Char(string="Test")
