from odoo import fields, models, api, _
from datetime import timedelta, date, datetime
from odoo.exceptions import ValidationError


class Instance_Request(models.Model):
    _name = "kzm.instance.request"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    _description = "creation d'instance"

    name = fields.Char(string="Designation", tracking=True)
    reference = fields.Char(string="Order Reference",
                            required=True, copy=False,
                            default=lambda self: _('New'))
    active = fields.Boolean(default=True)
    adress_ip = fields.Char(string="Adresse IP")
    cpu = fields.Char(string="CPU")
    ram = fields.Char(string="RAM")
    disk = fields.Char(string="DISK")
    url = fields.Char(string="URL")
    state = fields.Selection(
        selection=[('brouillon', 'Brouillon'), ('soumise', 'Soumise'), ('entraitement', 'En traitement'),
                   ('traite', 'Traitée')],
        default='brouillon', tracking=True)
    limit_date = fields.Date(tracking=True)
    treat_date = fields.Datetime()
    treat_duration = fields.Float()

    def action_draft(self):
        for x in self:
            x.state = 'brouillon'

    def action_submissive(self):
        for x in self:
            x.state = 'soumise'

    def action_processing(self):
        for x in self:
            x.state = 'entraitement'

    def action_treated(self):
        for x in self:
            x.state = 'traite'

    def action_scheduled(self):
        day = self.env['kzm.instance.request'].search([('limit_date', '<=', date.today() + timedelta(days=5))])
        for x in day:
            x.action_submissive()

    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('instance.reconcile') or _('New')
        res = super(Instance_Request, self).create(vals)
        return res

    def unlink(self):
        for x in self:
            if x.state != 'brouillon':
                raise ValidationError(_("Vous ne pouvez supprimer que les demande d’instance en état Brouillon !"))
            return super(Instance_Request, x).unlink()

    def write(self, vals):
        if vals.get('limit_date'):
            date_time_obj = datetime.strptime(vals['limit_date'], '%Y-%m-%d')
            d = date_time_obj.date()
            if d < date.today():
                raise ValidationError(_("Vous ne pouvez pas définir une date limite postérieure à aujourd’hui !!"))
        return super(Instance_Request, self).write(vals)

    # @api.multi
    # def write(self, vals):
    #     for x in self:
    #         if x.limit_date(datetime) < datetime.now():
    #             res = super(Instance_Request, self).write(vals)
    #             print("Vous ne pouvez pas définir une date limite postérieure à aujourd’hui !!")
    #             return res
