# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderLineAgent(models.Model):
    _inherit = 'sale.order.line'

    agent_product = fields.Many2one('agent.product')

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id',
                 'agent_product')
    def _compute_amount(self):
        """
        Override standard Odoo function for computing price_subtotal
        """

        # Call super function and compute all prices
        super(SaleOrderLineAgent, self)._compute_amount()

        for record in self:
            # If there is an agent for the product
            if record.agent_product:
                # Calculate discount
                record_discount = record.agent_product.agent_discount/100.0
                discount_sum = record.price_subtotal * record_discount

                # Calculate sum - discount sum
                record.price_subtotal = record.price_subtotal - discount_sum
            else:
                pass
