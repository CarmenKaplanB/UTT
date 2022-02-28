import web # IMPORTACCION DE WEB.

render = web.template.render("mvc/views/")

class Comunidad():
    
    def GET(self):
        try:
            return render.comunidad() # RETORNAMOS EL REDERIZADO.
        except Exception as e:
            return "Error " + str(e.args) # EN CASO DE ERRORES, LOS DEVOLVERA.