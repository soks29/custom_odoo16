# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"
    _order = "name"

    name = fields.Char(string="Name", required=True)
    _sql_constraints = [('fleet_state_name_type_unique', 'unique(name)', 'A property type name must be unique')]
    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. lower is better.")
    