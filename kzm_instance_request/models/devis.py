# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Order(models.Model):
    _inherit = 'sale.order'

    version_odoo_id = fields.Many2one(comodel_name="odoo.version", string="Id odoo version")

    def add_instance(self):
        action = self.env.ref('kzm_instance_request.create_bons_commande_wizard').read()[0]
        return action
