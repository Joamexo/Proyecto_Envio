# -*- coding: utf-8 -*-
# from odoo import http


# class GestionProducto(http.Controller):
#     @http.route('/gestion__producto/gestion__producto', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion__producto/gestion__producto/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion__producto.listing', {
#             'root': '/gestion__producto/gestion__producto',
#             'objects': http.request.env['gestion__producto.gestion__producto'].search([]),
#         })

#     @http.route('/gestion__producto/gestion__producto/objects/<model("gestion__producto.gestion__producto"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion__producto.object', {
#             'object': obj
#         })
