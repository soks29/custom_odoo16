# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class KzmInstanceRequest(http.Controller):
    @http.route('/instance/ask', website=True, auth='public')
    def index(self, **kw):
        instance_r = request.env['kzm.instance.request'].sudo().search([])
        print("instance----", instance_r)
        return request.render("kzm_instance_request.example1", {
            'name': instance_r
        })
        # return "Hello, world"

#     @http.route('/kzm_instance_request/kzm_instance_request/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kzm_instance_request.listing', {
#             'root': '/kzm_instance_request/kzm_instance_request',
#             'objects': http.request.env['kzm_instance_request.kzm_instance_request'].search([]),
#         })

#     @http.route('/kzm_instance_request/kzm_instance_request/objects/<model("kzm_instance_request.kzm_instance_request"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kzm_instance_request.object', {
#             'object': obj
#         })
