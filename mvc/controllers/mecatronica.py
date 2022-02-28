import web # IMPORTACCION DE WEB.

render = web.template.render("mvc/views/")

class Mecatronica():
    
    def GET(self):
        try:
            return render.mecatronica() # RETORNAMOS EL REDERIZADO.
        except Exception as e:
            return "Error " + str(e.args) # EN CASO DE ERRORES, LOS DEVOLVERA.