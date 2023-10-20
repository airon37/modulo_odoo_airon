# -*- coding: utf-8 -*-
# from odoo import http


# class AironSanchez(http.Controller):
#     @http.route('/airon_sanchez/airon_sanchez', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/airon_sanchez/airon_sanchez/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('airon_sanchez.listing', {
#             'root': '/airon_sanchez/airon_sanchez',
#             'objects': http.request.env['airon_sanchez.airon_sanchez'].search([]),
#         })

#     @http.route('/airon_sanchez/airon_sanchez/objects/<model("airon_sanchez.airon_sanchez"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('airon_sanchez.object', {
#             'object': obj
#         })
