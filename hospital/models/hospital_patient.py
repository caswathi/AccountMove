from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api


class Hospital(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _rec_name = 'patient_id'

    patient_id = fields.Char(string="PATIENT ID", readonly=True, required=True,
                             copy=False, default='New')
    partner_id = fields.Many2one('res.partner', string="Name",
                                 required=True)
    patient_gender = fields.Selection(related='partner_id.gender',
                                      string="Gender")
    patient_dob = fields.Date(related='partner_id.dob', string="Date Of Birth")
    age = fields.Char(string="Age")
    pat_mobile = fields.Char(string="Mobile", related='partner_id.mobile')
    pat_phone = fields.Char(string="Phone", related='partner_id.phone')
    blood_group = fields.Selection(
        [('O+', 'O+ve'), ('O-', 'O-ve'), ('B-', 'B-ve'), ('B+', 'B+ve'),
         ('AB+', 'AB+ve'), ('AB-', 'AB-ve')], string="Blood Group",
        required=True)
    op_lines = fields.One2many('hospital.op', 'patient_id', string="OP ID")

    @api.model
    def create(self, vals):
        print(self.ids)
        vals['patient_id'] = self.env['ir.sequence'].next_by_code(
            'self.service')
        print(vals['patient_id'])
        result = super(Hospital, self).create(vals)
        return result

    @api.onchange('patient_dob')
    def _onchange_patient_dob(self):
        for rec in self:
            if rec.patient_dob:
                dt = rec.patient_dob
                d2 = date.today()
                rd = relativedelta(d2, dt)
                rec.age = str(rd.years) + ' years'



