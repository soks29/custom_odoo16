# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class KzmInstanceCreationPortal(http.Controller):
    @http.route('/instance/ask', website=True, auth='public')
    def index(self):
        create_id = request.env.context.get('uid')
        instances = http.request.env['kzm.instance.request'].search([('create_uid', '=', create_id)])
        return http.request.render('kzm_instance_creation_portal.portal_instance_request', {
            'instances': instances,
            'page_name': 'instance'
        })

    @http.route('/instance_webform', type="http", auth="public", website=True)
    def instance_webform(self, **kw):
        return http.request.render('kzm_instance_creation_portal.template_create_instance1', {})

    @http.route('/create/web_instance', type='http', auth='public', website=True)
    def create_instances_portal(self, **kw):
        request.env['kzm.instance.request'].sudo().create(kw)
        return request.render('kzm_instance_creation_portal.portal_instance_request', {
        })

# class KzmInstanceCreationPortal(http.Controller):
#     @http.route('/kzm_instance_creation_portal/kzm_instance_creation_portal', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kzm_instance_creation_portal/kzm_instance_creation_portal/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kzm_instance_creation_portal.listing', {
#             'root': '/kzm_instance_creation_portal/kzm_instance_creation_portal',
#             'objects': http.request.env['kzm_instance_creation_portal.kzm_instance_creation_portal'].search([]),
#         })

#     @http.route('/kzm_instance_creation_portal/kzm_instance_creation_portal/objects/<model("kzm_instance_creation_portal.kzm_instance_creation_portal"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kzm_instance_creation_portal.object', {
#             'object': obj
#         })
