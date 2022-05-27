# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'
    _description = 'Product warranty'
    date_from = fields.Date('From')
    date_to = fields.Date('To')
    product_warranty_code = fields.Char("PW CODE", compute='check_code')
    check_valid_date = fields.Boolean(string='Check Valid', compute='check_date')
    total = fields.Monetary("discount estimated", compute='check_total')
    discount = fields.Char('Discount', default="")
    calculated_discount_total = fields.Monetary('discount total')

    @api.constrains('date_from', 'date_to')
    def check_date_warranty(self):
        if self.date_to < self.date_from:
            raise models.ValidationError('We need a day in future like tomorrow!')

    @api.depends('date_from', 'date_to', 'product_warranty_code')
    def check_code(self):
        for record in self:
            date_from_str = str(record.date_from)
            date_to_str = str(record.date_to)
            code_from = date_from_str.replace('-', '')
            code_to = date_to_str.replace('-', '')
            record.product_warranty_code = "PWR/" + code_from + "/" + code_to

    @api.depends('product_warranty_code', 'discount')
    def check_date(self):
        for record in self:
            if record.product_warranty_code != "PWR/False/False":
                record.check_valid_date = True
                for rec in self:
                    if rec.check_valid_date:
                        rec.discount = 0
                        rec.total = rec.standard_price
            else:
                record.check_valid_date = False

    @api.depends('total')
    def check_total(self):
        for rec in self:
            if not rec.date_to:
                rec.discount = "10%"
                rec.total = rec.standard_price - rec.standard_price * 10 / 100
                rec.calculated_discount_total = rec.standard_price * 10 / 100
            else:
                rec.discount = ""
                rec.total = rec.standard_price

    def action_confirm(self):
        for rec in self:
            rec.date_from = fields.Date.today()
            rec.date_to = fields.Date.today() + timedelta(days=365)


