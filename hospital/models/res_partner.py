from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    dob = fields.Date(string="Date of Birth", help="Date of Birth")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'),
                               ('other', 'Other')], string="Gender")




