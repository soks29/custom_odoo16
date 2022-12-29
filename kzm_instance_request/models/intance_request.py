from odoo import fields, models

class Instance_Request(models.Model):
    _name = "kzm.instance.request"
    _description = "creation d'instance"

    name = fields.Char("Designation", required=True)
    active = fields.Boolean(default=True)
    adress_ip = fields.Char("Adress IP")
    cpu = fields.Char()
    ram = fields.Char()
    disk = fields.Char()
    url = fields.Char()
    state = fields.Selection(
        selection=[('state1','Brouillon'),('state2','Soumise'),('state3','En traitement'),('state4','Traitée')],
        default='state1')
    limit_date = fields.Date(required=True)
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
