# -*- coding: utf-8 -*-

from odoo import models, fields, api

#esto seria la configuracion basica de un modelo en odoo
class Visit(models.Model):
     _name = 'custom_crm.visit' #sigue un estandar en donde ponemos, el nombre del modulo, y el nombre del modelo
     _description = 'Visit' #descripcion, cualquier descripcion que describa el modelo

     name = fields.Char(string='Descripcion') #lo que va dentro de los parentesis es como va a quedar definido en la vista del crm
     customers = fields.Char(string='Cliente')
     date = fields.Datetime(string='Fecha')
     type = fields.Selection([('P', 'Presencial'), ('W', 'Whatsapp'), ('T', 'Telefonico')], string='Tipo', required=True) #required es un tipo de dato requerido, que siempre se debe especificar
     done = fields.Boolean(string='Realizada', readonly=True) #readnoly significa que ese valor de realizada, no se va a poder modificar desde la vista presentada pues en el navegador

#     @api.depends('value')
#     def _value_pc(self):