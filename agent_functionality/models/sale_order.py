# -*- coding: utf-8 -*-

from odoo import models, fields, api
from openerp.exceptions import Warning

class SaleOrderCancel(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_cancel(self):
        super(SaleOrderCancel, self).action_cancel()
        connected_invoices = self.mapped('invoice_ids')
        if connected_invoices:
            paid_invoices = connected_invoices.search([('state', '=', 'paid')])
            connected_invoices.mapped(lambda x: x.write({'state': 'cancel'}))

            if paid_invoices:
                raise Warning('We have cancelled some paid invoices')
