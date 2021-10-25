from odoo import models, fields


class HospitalOp(models.Model):
    _name = 'hospital.op'
    _description = 'Hospital OP'
    _rec_name = 'token'

    patient_id = fields.Many2one('hospital.patient', string="Patient Card",
                                 required=True)
    pname = fields.Char(related='patient_id.partner_id.name')
    p_age = fields.Char(related='patient_id.age')
    p_gender = fields.Selection(related='patient_id.partner_id.gender')
    blood_group = fields.Selection(related='patient_id.blood_group')
    employee_id = fields.Many2one('hr.employee', domain=[('job_id', '=', 1)],
                                  string="Doctor", required=True)
    token = fields.Integer(related='employee_id.associate_count',
                           store=True, copy=False, string="Token")
    current_date = fields.Date(string="Date", default=fields.date.today(),
                               store=True)
    currency_id = fields.Many2one('res.currency', string="Currency")
    fees = fields.Float(related='employee_id.fees', string="Fees")
    status = fields.Selection(selection=[('draft', 'Draft'),
                                         ('confirmed', 'Confirmed')],
                              default='draft', copy=False)

    def button_confirm(self):
        self.write({'status': 'confirmed'})

    def button_reset(self):
        self.write({'status': 'draft'})

    def button_payment(self):
        view_id = self.env.ref('account.view_move_form').id
        context = {
            'default_move_type': 'out_invoice',
            'default_partner_id': self.patient_id.partner_id.id,
            'default_invoice_date': fields.datetime.today(),
            'default_journal_id': 8,
            'default_line_ids': [{
                'price_unit': self.fees,
                'quantity': 1,
            }]
        }
        return {
            'name': 'Invoice',
            'view_type': 'form',
            'view_mode': 'tree',
            'views': [(view_id, 'form')],
            'res_model': 'account.move',
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'target': 'current',
            'context': context,
        }

