from odoo import models, fields


class HospitalDisease(models.Model):
    _name = 'hospital.disease'
    _description = 'Diseases'

    name = fields.Char(string="Disease")
