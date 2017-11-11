# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Agent(models.Model):
    _inherit = 'res.partner'

    is_agent = fields.Boolean(string='Is agent')
