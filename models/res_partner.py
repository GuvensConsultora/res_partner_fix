from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    x_no_saldo_favor = fields.Boolean(
        string="No saldo a favor",
        default=False
    )
