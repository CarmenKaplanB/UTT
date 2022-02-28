import web # IMPORTACCION DE WEB.

render = web.template.render("mvc/views/")

class Enfermeria():
    
    def GET(self):
        try:
            return render.enfermeria() # RETORNAMOS EL REDERIZADO.
        except Exception as e:
            return "Error " + str(e.args) # EN CASO DE ERRORES, LOS DEVOLVERA.