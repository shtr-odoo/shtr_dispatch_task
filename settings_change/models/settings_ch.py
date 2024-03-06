from odoo import models,fields,api
from odoo.exceptions import UserError

class SettingsCh(models.TransientModel):
     _inherit = "res.config.settings"


     module_stock_transport = fields.Boolean(string="Dispatch Management System")

     