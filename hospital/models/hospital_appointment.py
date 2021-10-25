from datetime import datetime

from odoo import models, fields, api


class HospitalAppointment(models.Model):
    _name = 'hospital.appointmentt'
    _description = 'Appointment'
    _rec_name = 'appointment_id'

    appointment_id = fields.Char(string="AppointmentId", readonly=True,
                                 required=True, copy=False, default='New')
    patient_id = fields.Many2one('hospital.patient', required=True,
                                 string="Patient Card")
    patient_name = fields.Char(related='patient_id.partner_id.name')
    employee_id = fields.Many2one('hr.employee', domain=[('job_id', '=', 1)],
                                  string="Doctor", required=True)
    department = fields.Char(related='employee_id.department_id.name',
                             string="Department")
    date = fields.Date(string="Date", default=datetime.today(), store=True)
    state = fields.Selection(selection=[('draft', 'Draft'),
                                        ('appointment', 'Appointment'),
                                        ('op', 'OP')], default='draft')
    op_count = fields.Integer(compute='compute_op_count')
    token = fields.Integer(related='employee_id.associate_count', store=True,
                           copy=False, string="Token", readonly=True)

    def button_confirm(self):
        self.token = self.token + 1
        self.write({'state': 'appointment'})

    # def button_reset(self):
    #     self.token = self.employee_id.associate_count - 1
    #     self.write({'state': 'draft'})

    def button_op(self):
        self.write({'state': 'op'})
        res = {
            'name': 'OP Sub',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'hospital.op',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': 'current',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_employee_id': self.employee_id.id,
                'default_status': 'confirmed',
                'default_token': self.token
            }
        }
        print(type(res))
        return res

    @api.model
    def create(self, vals):
        print(self.ids)
        vals['appointment_id'] = self.env['ir.sequence'].next_by_code(
            'appointment_sequence')
        print(vals['appointment_id'])
        result = super(HospitalAppointment, self).create(vals)
        return result

    def get_op(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'OP',
            'view_mode': 'tree',
            'res_model': 'hospital.op',
            'domain': [('patient_id.partner_id.id',
                        '=',
                        self.patient_id.partner_id.id)],
            'context': "{'create': False}"
        }

    @api.depends('patient_id')
    def compute_op_count(self):
        for record in self:
            record.op_count = self.env['hospital.op'].search_count([(
                'patient_id.partner_id.id',
                '=',
                self.patient_id.partner_id.id)])
