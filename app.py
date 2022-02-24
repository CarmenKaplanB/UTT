import web

urls = [
    '/','mvc.controllers.index.Index', 
    '/index/?','mvc.controllers.index.Index',
    '/profile/?','mvc.controllers.profile.Profile',
    '/conocenos/?','mvc.controllers.conocenos.Conocenos'

    ] # COLOCAMOS LA RUTA

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()