# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re
from odoo import exceptions


class ListDiscountCode(models.Model):
    _name = "list.discount.code"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "List discount code"
    _rec_name = 'customer_discount_code'
    customer_discount_code = fields.Text('Detail Code', required=True)
    exp_date = fields.Datetime('EXP', default=fields.Date.today(), tracking=True)
    mfg_date = fields.Datetime('MFG', tracking=True)
    is_used = fields.Boolean('Selected')

    @api.model
    def update_selected_code(self):
        is_code = self.env['sale.order'].sudo().search([])
        for rec in self:
            for rec2 in is_code:
                if rec.customer_discount_code == rec2.code_id.customer_discount_code:
                    rec.is_used = True

    @api.constrains('exp_date', 'mfg_date')
    def check_date(self):
        if self.mfg_date < self.exp_date:
            raise models.ValidationError('We need a day in future like tomorrow!')