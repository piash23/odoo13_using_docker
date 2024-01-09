from odoo import _, api, fields, models


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):
        res = super(ResPartnerInherit, self).create(vals)
        print("Create: ", res)
        return res


class SalesOrderInherit(models.Model):
    _inherit = 'sale.order'

    patient_name = fields.Char(string="Patient Name")


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # _rec_name = 'patient_name'

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s - %s' % (rec.patient_name, rec.patient_age)))
        return res

    patient_name = fields.Char(string="Patient Name", required=True, track_visibility='always')
    patient_age = fields.Integer(string="Age", track_visibility='always')
    notes = fields.Text(string='Notes')
    image = fields.Binary(string="Image")
    name = fields.Char(string="Test")
    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))

    patient_gender = fields.Selection([('male', "Male"), ('fe_male', 'Female')], string="gender", default='male')
    age_group = fields.Selection([('major', 'Major'), ('minor', 'Minor')], string="Age Group", compute='set_age_group')
    appointment_count = fields.Integer(string="Appointment", compute='get_appointment_count')
    active = fields.Boolean(string="Active", default=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    doctor_gender = fields.Selection(string='Doctor\'s gender', selection=[('male', 'Male'), ('female', 'Female'), ])
    user_id = fields.Many2one('res.users', string='PRO', default=lambda self: self.env.user)
    contact_number = fields.Char(string='Contact Number')
    email = fields.Char(string='Email')
    patient_name_upper = fields.Char(compute='_compute_upper_name', inverse='_inverse_upper_name')


    @api.depends('patient_name')
    def _compute_upper_name(self):
        for rec in self:
            rec.patient_name_upper = rec.patient_name.upper()

    def _inverse_upper_name(self):
        for rec in self:
            rec.patient_name = rec.patient_name_upper.capitalize()

    @api.onchange('doctor_id')
    def set_doctor_gender(self):
        self.doctor_gender = self.doctor_id.gender

    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age > 18:
                rec.age_group = 'major'
            else:
                rec.age_group = 'minor'

    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age < 5:
                raise models.ValidationError("The age must be greater than 5")

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code(
                'hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result

    def get_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.appointment_count = count

    def open_patient_appointment(self):
        return {
            'name': _('Appointment'),
            'domain': [('patient_id', '=', self.id)],
            'res_model': 'hospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window'
        }

    def send_by_email(self):
        template_id = self.env.ref('om_hospital.email_template_patient_card').id
        self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)
        ctx = {
            'default_model': 'hospital.patient',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'custom_layout': "mail.mail_notification_paynow",
            'proforma': self.env.context.get('proforma', False),
            'force_email': True,
            # 'model_description': self.with_context(lang=lang).type_name,
        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }
