from odoo import api, fields, models


class OdooVersionHerit(models.Model):
    _inherit = ['odoo.version']

    instance_ids = fields.One2many(string="Request for creations", comodel_name='kzm.instance.request')
    nbre_instance_ids = fields.Integer(string="Number of instances", compute="comp_nbre_instance")

    def comp_nbre_instance(self):
        for x in self:
            x.nbre_instance_ids = len(x.instance_ids)
