# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class BonsCommandeVentes(models.TransientModel):
    _name = 'create.bons.command'

    cpu = fields.Char(string="CPU")
    ram = fields.Char(string="RAM")
    disk = fields.Char(string="DISK")
    tl_id = fields.Many2one(string="Employees", comodel_name='hr.employee')
    limit_date = fields.Date(string="Limit date", tracking=True)
    url = fields.Char(string="URL")

    def default_sale_order(self):
        for x in self:
            return x.env['sale.order'].browse(self._context.get('active_ids'))

    sale_ids = fields.Many2many(comodel_name="sale.order", string="Sale Order", required=True,
                                default=default_sale_order)

    def create_bons_commande(self):
        domain = [('tl_id', '=', self.tl_id)]
        if self.cpu <= 0 or self.disk <= 0 or self.ram <= 0:
            raise ValidationError(_("You cannot request instances with zero performance"))
        for x in range(len(self.purchase_orders)):
            self.env['kzm.instance.request'].create({
                'name': self.name,
                'cpu': self.cpu,
                'disk': self.disk,
                'url': self.url,
                'limit_date': self.limit_date,
                'tl_id': self.tl_id.id,
            })

        return {
            'name': _('list of instance created'),
            'res_model': 'kzm.instance.request',
            'view_mode': 'tree, form',
            'context': {},
            'domain': domain,
            'type': 'ir.actions.act_window',
            'views': [(self.env.ref('kzm_instance_request.kzm_instance_request_list_view').id, 'tree')]
        }
