from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    is_doctor = fields.Boolean(string="Is a Doctor", default=False)
    associate_count = fields.Integer(string="Count",
                                     compute='_compute_associate_count')
    employee_ids = fields.One2many('hospital.op', 'employee_id',
                                   string="Associate op")
    # op_id = fields.Many2one('hospital.op')
    doctor_ids = fields.One2many('hospital.appointmentt', 'employee_id',
                                 string="Associate appointment")
    fees = fields.Float(string="Fees")

    def _compute_associate_count(self):
        self.associate_count = 1
        for i in self.employee_ids:
            print(i.current_date)
            incidents = self.env['hospital.op'].search_count([
                ('employee_id', '=', self.id),
                ('current_date', '=', i.current_date)])
            self.associate_count = incidents

