from odoo import _, api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "id desc"

    name = fields.Char(string="Appointment ID", required=True, copy=False, readonly=True,
                          index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    patient_age = fields.Integer(string="Age", related='patient_id.patient_age', readonly=True)
    notes = fields.Text(string='Notes')
    appointment_date = fields.Date(string="Date", required=True)
    state = fields.Selection([
        ('draft','Draft'), ('confirm', 'Confirm'), ('done', 'Done'), ('cancel', 'Cancel')], default='draft', string="Status")
    doctor_note = fields.Text(string="Doctor's Note")
    prescription = fields.Text(string="Prescription")
    appointment_line_ids = fields.One2many('hospital.appointment.lines', 'appointment_id', string="Appointment Lines")


    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'hospital.appointment.sequence') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result

    def write(self, values):
        res = super(HospitalAppointment, self).write(values)
        print("Test Write Method")
        return res

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'
    
    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
    
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'


class HospitalAppointmentLines(models.Model):
    _name = "hospital.appointment.lines"
    _description = "Appointment Lines"

    product_id = fields.Many2one('product.product', string="Medicine", required=True)
    product_qty = fields.Integer(string="Quantity")
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
