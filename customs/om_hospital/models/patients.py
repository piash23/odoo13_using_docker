from odoo import _, api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _rec_name = 'patinet_name'

    patinet_name = fields.Char(string="Patient Name", required=True)
    patinet_age = fields.Integer(string="Age")
    notes = fields.Text(string='Notes')
    image = fields.Binary(string="Image")
    name = fields.Char(string="Test")
    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    
    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code(
                'hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result

