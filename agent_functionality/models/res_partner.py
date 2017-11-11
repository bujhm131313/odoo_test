# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Agent(models.Model):
    _inherit = 'res.partner'

    is_agent = fields.Boolean(string='Is agent')
    agent_products = fields.One2many('agent.product', inverse_name='partner')
