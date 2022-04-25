from odoo import api, fields, models

class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    old_id = fields.Char(string='Old ID')