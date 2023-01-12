# -*- coding: utf-8 -*-
# from odoo import http


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
