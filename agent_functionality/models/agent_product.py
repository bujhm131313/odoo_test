# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AgentProduct(models.Model):
    _name = 'agent.product'

    partner = fields.Many2one('res.partner', string='Agent')
    product = fields.Many2one('product.product', string='Product')
    agent_discount = fields.Integer()
