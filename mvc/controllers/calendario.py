import web # IMPORTACCION DE WEB.

render = web.template.render("mvc/views/")

class Calendario():
    
    def GET(self):
        try:
            return render.calendario() # RETORNAMOS EL REDERIZADO.
        except Exception as e:
            return "Error " + str(e.args) # EN CASO DE ERRORES, LOS DEVOLVERA.