from odoo import fields, models
from datetime import timedelta, date


class Instance_Request(models.Model):
    _name = "kzm.instance.request"
    _description = "creation d'instance"

    name = fields.Char("Designation")
    active = fields.Boolean(default=True)
    adress_ip = fields.Char("Adress IP")
    cpu = fields.Char()
    ram = fields.Char()
    disk = fields.Char()
    url = fields.Char()
    state = fields.Selection(
        selection=[('state1','Brouillon'),('state2','Soumise'),('state3','En traitement'),('state4','Traitée')],
        default='state1')
    limit_date = fields.Date()
    treat_date = fields.Datetime()
    treat_duration = fields.Float()

    def action_draft(self):
        self.state = "state1"

    def action_submissive(self):
        self.state = "state2"

    def action_processing(self):
        self.state = "state3"

    def action_treated(self):
        self.state = "state4"

    def action_confirm(self):
        self.state = "state4"

    def action_scheduled(self):
        day = self.env['kzm.instance.request'].search([('limit_date', '<=', date.today() + timedelta(days=5))])
        for x in day:
            x.state = 'state2'

        # tmp1 = self.treat_date
        # tmp2 = self.limit_date(datetime)
        # days = tmp1 - tmp2
        # if days >= 5:
        #     self.state = "state2"