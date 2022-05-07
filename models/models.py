# -*- coding: utf-8 -*-

#Lo primero que hago apenas creo un proyecto para un modulo de odoo aqui en pycharm es crear una estructura para mi proyecto o modulo
#algo asi como una plantilla , en este caso utilizo algo llamado scaffold
# Aqui esta la documentacion para hacer el proceso: https://www.odoo.com/documentation/15.0/es/developer/misc/other/cmdline.html#reference-cmdline-scaffold


from odoo import models, fields, api
import datetime

#esto seria la configuracion basica de un modelo en odoo
class Visit(models.Model): #Aqui vamos a usar el tipo de modelo model, que es el estandar para crear modelos en odoo, casi en el 90% de los casos
     _name = 'custom_crm.visit' #sigue un estandar en donde ponemos, el nombre del modulo, y el nombre del modelo
     _description = 'Visit' #descripcion, cualquier descripcion que describa el modelo

     name = fields.Char(string='Descripcion') #lo que va dentro de los parentesis es como va a quedar definido en la vista del crm, como atributo le pasamos un string para que nos etiquete este campo

     #De esta manera relacioné un cliente con la visita: (Tema relaciones)
     customer = fields.Many2one(string='Cliente', comodel_name = 'res.partner') #El cliente en este caso lo vamos a asociar con N visitas. Será una relacion ManytoOne
     #Lo que hacemos con el Many2One es pintar a los clientes, dandome la lista para escoger el cliente.
     #el comodel_name es la tabla de la base de datos, quien tiene los registros de los clientes, el modelo de donde saldran los datos.
     date = fields.Datetime(string='Fecha')
     type = fields.Selection([('P', 'Presencial'), ('W', 'Whatsapp'), ('T', 'Telefonico')], string='Tipo', required=True) #required es un tipo de dato requerido, que siempre se debe especificar. Tambien se hace un arreglo de tuplas.
     done = fields.Boolean(string='Realizada', readonly=True) #readnoly significa que ese valor de realizada, no se va a poder modificar desde la vista presentada pues en el navegador

#     @api.depends('value')
#     def _value_pc(self):

#Imagen asociad a vista kamban
     image = fields.Binary(String='Imagen')

     """
          Que es un ORM?
               Un ORM lo que nos permite , en un paradigma de orientacion a objetos, tratar la base de datos las consultas a la base de datos
               como si fueran objetos. Osea que no tendriamos que escribir las sentencias sql como tal sino que nos vamos a valer de diferentes
               funciones que nos proovee este ORM para tratar con las entidades de la base de datos.
               
               NOTA: En base de datos, una entidad es una cosa u objeto del mundo real que es diferente de los demás objetos o cosas. Una entidad posee un conjunto de propiedades y los valores de estas propiedades identifican y distinguen a cada entidad de las otras.  
               En resumen una entidad puede ser una tabla en la base de datos, que puede o no estar relacionada con otras, y esta entidad podriamos tratarla como objeto segun el paradigma orientado a objetos
               
     """

     #ORM CREAR:
     #Ahora lo que haremos será crear una nueva funcion en python para el boton de crear

     def f_create(self): #definimos la funcion, le dimos un nombre y el self se lo dejamos por defecto
          visit ={
               'name': 'ORM test', #Le damos un nombre
               'customer': 1, #Aqui le tendriamos que especificar el id de base de datos. Se hace por id , ya que es una clave externa

               #NOTA: Hacer un cast o casting significa convertir un tipo de dato a otro. Anteriormente hemos visto tipos como los int, string o float. Pues bien, es posible convertir de un tipo a otro.
               #     Para el caso de str devuelve una cadena de string del objeto pasado como parametro.
               #    documentacion: https://www.programiz.com/python-programming/methods/built-in/str

               'date': str(datetime.date(2020, 8, 6)), #Las fechas tienen en cuenta la configuracion horaria del sistema
               'type': 'P', #Le pasamos el tipo, en este caso el tipo de la visita es presencial, por tanto ponemos una P, para que nos devuelva "Presencial"
               'done': False

               #De esta manera definimos la entidad visit en base de datos, osea que estos son los datos que guardaremos en la base de datos.

          }#creamos o definimos una nueva entidad apartir de un jason = js.
          #para este caso, los js en python los definimos como diccionarios

          #Imprimimos el anterior js, si queremos saber si se esta representando bien.
          print(visit)

          #Ahora si procedemos a guardar en la base de datos la informacion o la entidad creada apartir de este js.
          #Utilizamos para esto uno de los metodos que nos proporciona el ORM, en este caso el metodo create.
          #esto se hace a traves de la siguiente 'sentencia':
          #self.env['Aqui ponemos el nombre del modelo']. Invocamos el metodo, que en este caso es el create (Aqui en parentecis le pasamos el js que acabamos de crear, osea la entidad que queremos que nos guarde en la base de datos)
          self.env['custom_crm.visit'].create(visit)

     #ORM BUSCAR Y EDITAR

     def f_search_update(self):
          #Buscar
          #Primero haremos la busquedas. Para este ejemplo, haremos la busqueda de la entidad Visit que acabamos de agregar a la base de datos en la funcion anterior con el metodo create
          #Usaremos el metodo search para buscar, al cual le especificamos un array de tuplas en el cual especificamos las condiciones de busqueda que queremos aplicar
          visit = self.env['custom_crm.visit'].search([('name', '=', 'ingeniero WILSON')]) #El self.env se utiliza para llamar al método ORM directamente desde un objeto, el metodo orm vendria siendo en este caso search
          #El primer atributo que queremos utilizar para realizar la busqueda es el name osea que el nombre de la entidad sea igual en este caso, a la descripcion
          print('search()', visit, visit.name) #decimos que nos imprima el metodo search, solo el nombre  y que nos imprima la visita con el identificador en base de datos, y tambien que nos imprima el nombre de la visita

          #Luego usaremos el browser, el cual le pasamos un array con una serie de identificadores, los identificadores en base de datos de esas entidades
          visit_b = self.env['custom_crm.visit'].browse([9]) #como parametro le pasemos el id que identifica esa entidad de la base de datos.
          print('browse()', visit_b, visit_b.name)

          #Editar
          #Ahora como hacer o modificar los valores de los registros previamente recuperados por el metodo buscar.
          visit.write({
               'name': 'ing. WILSON'
          })#Para este caso usamos el metodo write que es quien nos permite hacer la modificacion o actualizacion del registro o la entidad.
          #IMPORTANTE: Obvio debemos primero hacer la busqueda de en este caso el name, y luego de hacer esta busqueda, guardar el atributo en la variable visit, para que posteriormente cuando vayamos a realizar la edicion pues podamos llamar al metodo del ORM
          #El metodo write recibe un js tipo, como un diccionario de python.


