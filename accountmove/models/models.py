from odoo import models, fields, api
from odoo.tools import float_compare


class AccountMovee(models.Model):
    _inherit = 'account.move'

    related_sale_order = fields.Many2many('sale.order',
                                          string="Related Sale Order")

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        self.related_sale_order = self.env['sale.order'].search([
            ('partner_id', '=', self.partner_id.id),
            ('invoice_status', '=', 'to invoice')])
        order_lines = []
        source = []
        for i in self.related_sale_order:
            source.append(i.name)
            order_lines = i.order_line
            # Appending related sale order lines to invoice Lines
            invoice_line_ids = []
            for line in order_lines:
                invoice_line_ids.append((0, 0, {
                    'product_id': line.product_id.id,
                    'quantity': line.product_uom_qty,
                    'product_uom_id': line.product_uom,
                    'price_unit': line.price_unit,
                    'price_subtotal': line.price_subtotal,
                    'discount': line.discount,
                    'name': line.name,
                    'analytic_tag_ids': line.analytic_tag_ids,
                    'tax_ids': line.tax_id,
                    'analytic_account_id': line.analytic_tag_ids.analytic_distribution_ids.account_id,
                    'account_id': i.l10n_in_journal_id.default_account_id.id,
                    'currency_id': line.currency_id,
                    'product_uom_category_id': line.product_uom_category_id,
                    'price_total': line.price_total,
                    'partner_id': self.partner_id.id,
                    'company_id': self._compute_company_id(),
                    'credit': line.price_total,
                }))

            self.invoice_line_ids = invoice_line_ids
            # create invoices for sale orders
        for invoice_line in self.related_sale_order:
            invoice_line._create_invoices()

        # source doccument of invoice
        saleorders = ','.join(source)
        self.invoice_origin = saleorders
        # self._compute_qty_invoiced()
        # Amount total computation
        for rec in self.invoice_line_ids:
            self.amount_total = self.amount_total + rec.price_subtotal
        self._onchange_invoice_line_ids()

