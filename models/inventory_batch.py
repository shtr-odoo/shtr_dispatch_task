from odoo import models,fields,api


class InventoryBatch(models.Model):
     _inherit = "stock.picking.batch"


     dock = fields.Many2one('dock.model', string="Dock")
     vehicle = fields.Many2one('fleet.vehicle.model',string="Vehicle")
     vehicle_category = fields.Many2one('fleet.vehicle.model.category',string="Vehicle Category")
     weight = fields.Float(string="Weight" , readonly=True, compute='_compute_weight', store=True)
     volume = fields.Float(string="Volume", readonly=True, compute='_compute_volume', store=True)

     @api.depends('picking_ids')
     def _compute_weight(self):
          for batch in self:
               total_weight = 0.0
               max_weight = batch.vehicle_category.max_weight
               for picking in batch.picking_ids:
                    total_weight += picking.weight
               batch.weight = total_weight / max_weight if max_weight else 0.0

     @api.depends('picking_ids')
     def _compute_volume(self):
          for batch in self:
               total_volume = 0.0
               max_volume = batch.vehicle_category.max_volume
               for picking in batch.picking_ids:
                    total_volume += picking.volume
               batch.volume = total_volume / max_volume if max_volume else 0.0

