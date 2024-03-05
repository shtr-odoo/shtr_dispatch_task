from odoo import models,fields


class DockModel(models.Model):
    _name = 'dock.model'
    _description = "Reference Dock Module"

    itself = fields.Integer(string="Itself")