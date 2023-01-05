from odoo import api, fields, models


class EmployeesHerit(models.Model):
    _inherit = ['hr.employee']

    instance_ids = fields.One2many(string="Request for creations", inverse_name="tl_id", comodel_name='kzm.instance.request', tracking=True)
    nbre_instance_ids = fields.Integer(string="Number of instances", compute="comp_nbre_instance")

    @api.depends('instance_ids')
    def comp_nbre_instance(self):
        for x in self:
            x.nbre_instance_ids = len(x.instance_ids)

    def action_instances(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'kzm_instance_request',
            'res_model': 'kzm.instance.request',
            'domain': [('tl_id', '=', self.name)],
            'view_mode': 'tree,form',
            'target': 'current',
        }
    