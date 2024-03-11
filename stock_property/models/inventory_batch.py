from odoo import models,fields,api


class InventoryBatch(models.Model):
     _inherit = "stock.picking.batch"


     dock = fields.Many2one('dock.model', string="Dock")
     vehicle = fields.Many2one('fleet.vehicle.model',string="Vehicle")
     vehicle_category = fields.Many2one('fleet.vehicle.model.category',string="Vehicle Category")
     weight = fields.Float(string="Weight" , readonly=True, compute='_compute_weight_volume', store=True)
     volume = fields.Float(string="Volume", readonly=True, compute='_compute_weight_volume', store=True)
     no_line = fields.Integer(string="Lines" ,compute='_compute_transfer_line' ,store=True)
     no_transfer = fields.Integer(string="Transfer", compute='_compute_transfer_line' ,store=True)
     total_w = fields.Float(string="Total Weight")
     total_v = fields.Float(string="Total Volume")

     @api.depends('picking_ids','vehicle_category')
     def _compute_weight_volume(self):
          self.weight = 0
          self.volume = 0

          for record in self:
               self.total_w = sum((line.weight) for line in record.picking_ids)
               self.total_v = sum((line.volume) for line in record.picking_ids)

          if self.vehicle_category.max_weight > 0 : self.weight = (self.total_w / self.vehicle_category.max_weight)*100
          if self.vehicle_category.max_volume > 0 : self.volume = (self.total_v/ self.vehicle_category.max_volume)*100

     @api.depends('picking_ids','move_line_ids')
     def _compute_transfer_line(self):
          for batch in self:
               # Counting the number of transfers
               batch.no_transfer = len(batch.picking_ids)
               # Counting the number of lines
               batch.no_line = sum(len(picking.move_line_ids) for picking in batch.picking_ids) 

     

     @api.depends('weight', 'volume')
     def _compute_display_name(self):
        for record in self:
            record.display_name = record.name + " (" + str(format(record.weight,".2f")) + "kg, " + str(format(record.volume,".2f")) + "m3)"