# -*- coding: utf-8 -*-
from odoo import http

# class XlwtImage(http.Controller):
#     @http.route('/xlwt_image/xlwt_image/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xlwt_image/xlwt_image/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xlwt_image.listing', {
#             'root': '/xlwt_image/xlwt_image',
#             'objects': http.request.env['xlwt_image.xlwt_image'].search([]),
#         })

#     @http.route('/xlwt_image/xlwt_image/objects/<model("xlwt_image.xlwt_image"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xlwt_image.object', {
#             'object': obj
#         })