# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from . import list_code
import re


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    _description = 'Advanced Sale'
    code_id = fields.Many2one('list.discount.code', 'discount code')
    sale_order_discount_estimated = fields.Monetary('Price used discount', compute='get_cost')
    description_code = fields.Text('Description code')
    descr = fields.Html("Description")
    currency_id = fields.Many2one('res.currency')

    @api.depends('sale_order_discount_estimated', 'code_id')
    def get_cost(self):
        final_num = 1
        for rec in self:
            rec.sale_order_discount_estimated = rec.amount_total
            if rec.code_id:
                available_code = re.match("^VIP_+[0-9]+[0-9]", rec.code_id.customer_discount_code)
                if available_code:
                    for num in rec.code_id.customer_discount_code.split('_'):
                        if num[:2].isdigit():
                            final_num = float(num)
                            rec.sale_order_discount_estimated = float(rec.amount_total) - float(
                                rec.amount_total) * final_num / 100

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s" % record.name
            result.append((record.id, rec_name))
        return result

    def action_confirm(self):
        print("button")
