# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class BatchUpdate(models.TransientModel):
    _name = "sale.order.update"
    _description = "update code"
    code_ids = fields.Many2many("list.discount.code", string="code ids")

    def _get_default_codes(self):
        return self.env['list.discount.code'].browse(self.env.context.get('active_ids'))

    @api.model
    def multi_update(self):
       pass
