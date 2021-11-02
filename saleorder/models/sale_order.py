from odoo import models, fields, api
from collections import Counter


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def create_project(self):
        milestone_list = []
        for rec in self.order_line:
            milestone_list.append(rec.milestone)
        unique_milestone = Counter(milestone_list).keys()
        print(len(unique_milestone))
        res = self.env['project.project'].create({
            'partner_id': self.partner_id.id,
            'name': self.name,
            'task_count': len(unique_milestone)
        })
        for rec in unique_milestone:
            print(rec)
            res1 = self.env['project.task'].create({
                'name': "Milestone "+str(rec),
                'project_id': res.id,
            })
            for res2 in self.order_line:
                if res2.milestone == rec:
                    res3 = self.env['project.task'].create({
                        'name': res2.product_id.name,
                        'project_id': res.id,
                        'parent_id': res1.id,
                        'sale_line_id': res2.id,
                    })
        return res

