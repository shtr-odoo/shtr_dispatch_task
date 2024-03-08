from odoo import models,fields


class SettingsCh(models.TransientModel):
     _inherit = "res.config.settings"


     module_stock_transport = fields.Boolean(string="Dispatch Management System")

     