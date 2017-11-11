# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderLineAgent(models.Model):
    _inherit = 'sale.order.line'

    agent_product = fields.Many2one('agent.product')



