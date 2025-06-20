from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    transaction_number = fields.Char(string="Transaction Number")
