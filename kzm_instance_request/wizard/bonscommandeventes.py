# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class BonsCommandeVentes(models.TransientModel):
    _name = 'create.bons.commande'

    purchase_orders = fields.Many2many(comodel_name='sale.order', string="Purchase Orders", required=True,
                                       default='default_purchase_order')
    cpu = fields.Char(string="CPU")
    ram = fields.Char(string="RAM")
    disk = fields.Char(string="DISK")
    tl_id = fields.Many2one(string="Employees", comodel_name='hr.employee')
    partner_id = fields.Many2one(comodel_name="res.partner", string="Customer")
    odoo_id = fields.Many2one(comodel_name="odoo.version", string="Odoo version")
    limit_date = fields.Date(string="Limit date", tracking=True)
    url = fields.Char(string="URL")

    def default_purchase_order(self):
        return self.env['sale.order'].browse(self._context.get('active_ids'))

    def create_bons_commande(self):
        if int(self.cpu) < 0 or int(self.ram) < 0 or int(self.disk) < 0:
            raise ValidationError(_("You can't request instances with zero performance!"))
        for x in range(len(self.purchase_orders)):
            self.env['kzm.instance.request'].create({'cpu': self.cpu, 'ram': self.ram, 'disk': self.disk,
                                                     'partner_id': self.partner_id.id, 'odoo_id': self.odoo_id.id,
                                                     'tl_id': self.tl.id, 'limit_date': self.limit_date,
                                                     'url': self.url})

    # @api.model
    # def create_bons_commande(self, values):
    #     # Code before create
    #     from custom.addons import kzm_instance_request
    #     record = super(kzm_instance_request, self).create(values)
    #     # Code after create
    #     return record
