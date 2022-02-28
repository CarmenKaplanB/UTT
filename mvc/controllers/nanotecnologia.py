import web # IMPORTACCION DE WEB.

render = web.template.render("mvc/views/")

class Nanotecnologia():
    
    def GET(self):
        try:
            return render.nanotecnologia() # RETORNAMOS EL REDERIZADO.
        except Exception as e:
            return "Error " + str(e.args) # EN CASO DE ERRORES, LOS DEVOLVERA.