# -*- coding: utf-8 -*-
from odoo import http

# class ZoomImage(http.Controller):
#     @http.route('/zoom_image/zoom_image/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zoom_image/zoom_image/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('zoom_image.listing', {
#             'root': '/zoom_image/zoom_image',
#             'objects': http.request.env['zoom_image.zoom_image'].search([]),
#         })

#     @http.route('/zoom_image/zoom_image/objects/<model("zoom_image.zoom_image"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zoom_image.object', {
#             'object': obj
#         })