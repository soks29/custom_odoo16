# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag"
    _order = "name"

    name = fields.Char(string="Name", required=True)
    _sql_constraints = [('fleet_state_name_tag_unique', 'unique(name)', 'A property tag name must be unique')]
    color = fields.Integer(string="Color")
