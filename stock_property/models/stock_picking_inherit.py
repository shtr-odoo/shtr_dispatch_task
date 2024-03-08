from odoo import models,fields,api


class StockPickingIn(models.Model):
     _inherit = "stock.picking"

     volume = fields.Float(string='Volume' , compute="_compute_volume")
     weight = fields.Float(string='Weight', compute="_compute_weight")


     @api.depends('move_ids')
     def _compute_volume(self):
          for record in self:
               record.volume = sum((line.product_id.volume * line.product_uom_qty) for line in record.move_ids)

     @api.depends('move_ids')
     def _compute_weight(self):
          for record in self:
               record.weight = sum((line.product_id.weight * line.product_uom_qty) for line in record.move_ids)


     
    