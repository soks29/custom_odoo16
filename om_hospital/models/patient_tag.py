# -*- coding: utf-8 -*-
from datetime import date

from odoo import models, fields, api


class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient tag'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    color = fields.Integer(string="Color")
    color_2 = fields.Char(string="Color 2")

