# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AgentProduct(models.Model):
    _name = 'agent.product'

    partner = fields.Many2one('res.partner', string='Agent', readonly=True,
                              required=True)
    product = fields.Many2one('product.product', string='Product',
                              required=True, domain=[('type', '=', 'service')])
    agent_discount = fields.Integer(required=True)

    @api.multi
    def name_get(self):
        """
        Override standard name_get to change agent.product name view

        :return: list of tuples: [(id,name)]
        """
        res = []
        for record in self:
            name = "{0}, discount: {1}%".format(
                record.partner.name, record.agent_discount)
            res.append((record.id, name))

        return res
