from odoo import fields, models
from datetime import timedelta, date


class Instance_Request(models.Model):
    _name = "kzm.instance.request"
    _inherit = "mail.thread"
    _description = "creation d'instance"

    name = fields.Char(string="Designation")
    active = fields.Boolean(default=True)
    adress_ip = fields.Char(string="Adress IP")
    cpu = fields.Char(string="")
    ram = fields.Char(string="")
    disk = fields.Char(string="")
    url = fields.Char(string="")
    state = fields.Selection(
        selection=[('brouillon','Brouillon'),('soumise','Soumise'),('entraitement','En traitement'),('traite','Traitée')],
        default='brouillon')
    limit_date = fields.Date()
    treat_date = fields.Datetime()
    treat_duration = fields.Float()

    def action_draft(self):
        self.state = "brouillon"

    def action_submissive(self):
        self.state = "soumise"

    def action_processing(self):
        self.state = "entraitement"

    def action_treated(self):
        self.state = "traite"


    def action_scheduled(self):
        day = self.env['kzm.instance.request'].search([('limit_date', '<=', date.today() + timedelta(days=5))])
        for x in day:
            x.state = 'soumise'

        # tmp1 = self.treat_date
        # tmp2 = self.limit_date(datetime)
        # days = tmp1 - tmp2
        # if days >= 5:
        #     self.state = "state2"