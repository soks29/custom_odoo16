# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class BonsCommandeVentes(models.TransientModel):
    _name = 'create.bons.commande'

    purchase_orders = fields.Many2many(comodel_name='sale.order', string="Purchase Orders")
    cpu = fields.Char(string="CPU")
    ram = fields.Char(string="RAM")
    disk = fields.Char(string="DISK")
    tl_id = fields.Many2one(string="Employees", comodel_name='hr.employee')


    def create_bons_commande(self):
        for x in self:
            x.action = self.env.ref('kzm_instance_request.create_bons_commande_wizard').create()
        return x.action

    # @api.model
    # def create_bons_commande(self, values):
    #     # Code before create
    #     from custom.addons import kzm_instance_request
    #     record = super(kzm_instance_request, self).create(values)
    #     # Code after create
    #     return record
