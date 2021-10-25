from datetime import datetime
from odoo import models, fields, api


class HospitalConsultation(models.Model):
    _name = 'hospital.consultation'
    _description = 'Patient Consultation'
    _rec_name = 'consult_id'

    patient_card = fields.Many2one('hospital.patient', string="Patient Card",
                                   required=True)
    consultation_type = fields.Selection([('op', 'OP'), ('ip', 'IP')],
                                         string="Consultation Type",
                                         required=True)
    consult_date = fields.Date(string="Date", default=fields.Date.today(),
                               store=True)
    consult_doctor = fields.Many2one('hr.employee',
                                     domain=[('is_doctor', '=', 'True')],
                                     string="Doctor", required=True)
    department = fields.Char(string="Department",
                             related='consult_doctor.department_id.name')
    consult_disease = fields.Many2one('hospital.disease', string="Disease",
                                      required=True)
    diagnose = fields.Text(string="Diagnose")
    treatment_lines = fields.One2many('hospital.treatment',
                                      'treatment_id', string='Treatment lines')
    consult_id = fields.Char(string="CONSULTATION ID", readonly=True,
                             required=True, copy=False, default='New')

    @api.model
    def create(self, vals):
        print(self.ids)
        vals['consult_id'] = self.env['ir.sequence'].next_by_code(
            'consult_sequence')
        print(vals['consult_id'])
        result = super(HospitalConsultation, self).create(vals)
        return result


class TreatmentLines(models.Model):
    _name = 'hospital.treatment'
    _description = 'Treatment Lines'

    medicine_id = fields.Many2one('hospital.medicine', string="Medicine")
    med_dose = fields.Integer(related='medicine_id.medicine_dose')
    days = fields.Integer(string="Days")
    description = fields.Text(related='medicine_id.medicine_description')
    treatment_id = fields.Many2one('hospital.consultation',
                                   string="Treatment Id", ondelete='cascade')





