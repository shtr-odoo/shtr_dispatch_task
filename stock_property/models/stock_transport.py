from odoo import models,fields,api


class StockTransport(models.Model):
    _inherit = "fleet.vehicle.model.category"
      
    # adding new fields
    
    max_weight = fields.Float(string="Maximum Weight(Kg)")
    max_volume = fields.Float(string="Maximum Volume(m^3)")

    @api.depends('max_weight', 'max_volume')
    def _compute_display_name(self):
            for record in self:
                display_name = record.name
                display_name = f"{record.name}({record.max_weight} Kg), ({record.max_volume} m^3)"
                record.display_name = display_name

    
                                                                                                      
 





