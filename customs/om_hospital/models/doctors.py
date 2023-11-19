from odoo import _, api, fields, models

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "Doctor Record"


    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([('male', 'Male'),('female', 'Female')], string="Gender")
    user_id = fields.Many2one('res.users', string='Related User', required=True)
