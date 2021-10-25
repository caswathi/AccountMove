from odoo import models, fields, api


class HospitalMedicine(models.Model):
    _name = 'hospital.medicine'
    _description = 'Medicine'

    name = fields.Char(string="Name")
    medicine_company = fields.Char(string="Manufacture Company")
    medicine_cost = fields.Float(string="Cost")
    medicine_dose = fields.Integer(string="Dose")
    medicine_description = fields.Text(string="Description")
    medicine_id = fields.Char(string="MEDICINE ID", readonly=True,
                              required=True,
                              copy=False, default='New')

    @api.model
    def create(self, vals):
        print(self.ids)
        vals['medicine_id'] = self.env['ir.sequence'].next_by_code(
            'medicine_sequence')
        print(vals['medicine_id'])
        result = super(HospitalMedicine, self).create(vals)
        return result



