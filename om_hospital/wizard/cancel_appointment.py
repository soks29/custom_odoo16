# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
    raison = fields.Text(string="Raison")

    def action_cancel(self):
        pass
