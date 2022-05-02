# -*- coding: utf-8 -*-

#Lo primero que hago apenas creo un proyecto para un modulo de odoo aqui en pycharm es crear una estructura para mi proyecto o modulo
#algo asi como una plantilla , en este caso utilizo algo llamado scaffold
# Aqui esta la documentacion para hacer el proceso: https://www.odoo.com/documentation/15.0/es/developer/misc/other/cmdline.html#reference-cmdline-scaffold


from odoo import models, fields, api

#esto seria la configuracion basica de un modelo en odoo
class Visit(models.Model): #Aqui vamos a usar el tipo de modelo model, que es el estandar para crear modelos en odoo, casi en el 90% de los casos
     _name = 'custom_crm.visit' #sigue un estandar en donde ponemos, el nombre del modulo, y el nombre del modelo
     _description = 'Visit' #descripcion, cualquier descripcion que describa el modelo

     name = fields.Char(string='Descripcion') #lo que va dentro de los parentesis es como va a quedar definido en la vista del crm, como atributo le pasamos un string para que nos etiquete este campo
     customers = fields.Char(string='Cliente')
     date = fields.Datetime(string='Fecha')
     type = fields.Selection([('P', 'Presencial'), ('W', 'Whatsapp'), ('T', 'Telefonico')], string='Tipo', required=True) #required es un tipo de dato requerido, que siempre se debe especificar. Tambien se hace un arreglo de tuplas.
     done = fields.Boolean(string='Realizada', readonly=True) #readnoly significa que ese valor de realizada, no se va a poder modificar desde la vista presentada pues en el navegador

#     @api.depends('value')
#     def _value_pc(self):