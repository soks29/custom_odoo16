from odoo import fields, models
from datetime import timedelta, date


class Instance_Request(models.Model):
    _name = "kzm.instance.request"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    _description = "creation d'instance"

    name = fields.Char(string="Designation", tracking=True)
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