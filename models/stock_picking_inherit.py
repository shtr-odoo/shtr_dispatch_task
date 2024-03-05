from odoo import models,fields,api


class StockPickingIn(models.Model):
     _inherit = "stock.picking"

     volume = fields.Float(string='Volume')
     weight = fields.Float(string='Weight')


     


     
    