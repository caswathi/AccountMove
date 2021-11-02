from odoo import models, fields


class SaleOrderline(models.Model):
    _inherit = 'sale.order.line'

    milestone = fields.Integer(string='Milestone')

