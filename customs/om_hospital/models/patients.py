from odoo import _, api, fields, models


class SalesOrderInherit(models.Model):
    _inherit = 'sale.order'

    patient_name = fields.Char(string="Patient Name")


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _rec_name = 'patient_name'

    patient_name = fields.Char(string="Patient Name", required=True)
    patient_age = fields.Integer(string="Age")
    notes = fields.Text(string='Notes')
    image = fields.Binary(string="Image")
    name = fields.Char(string="Test")
    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))

    patient_gender = fields.Selection([('male', "Male"),('fe_male', 'Female')], string="gender", default='male')
    age_group = fields.Selection([('major', 'Major'), ('minor', 'Minor')], string="Age Group", compute='set_age_group')

    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age > 18:
                rec.age_group = 'major'
            else:
                rec.age_group = 'minor'
    
    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code(
                'hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result

