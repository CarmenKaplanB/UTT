import web # IMPORTACCION DE WEB.

render = web.template.render("mvc/views/")

class Reproductiva():
    
    def GET(self):
        try:
            return render.reproductiva() # RETORNAMOS EL REDERIZADO.
        except Exception as e:
            return "Error " + str(e.args) # EN CASO DE ERRORES, LOS DEVOLVERA.