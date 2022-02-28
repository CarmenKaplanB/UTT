import web

urls = [
    '/','mvc.controllers.index.Index',
    '/calendario/?','mvc.controllers.calendario.Calendario',
    '/comunidad/?','mvc.controllers.comunidad.Comunidad',
    '/conocenos/?','mvc.controllers.conocenos.Conocenos',
    '/contaduria/?','mvc.controllers.contaduria.Contaduria',
    '/criminalistica/?','mvc.controllers.criminalistica.Criminalistica',
    '/desarrollo/?','mvc.controllers.desarrollo.Desarrollo',
    '/digital/?','mvc.controllers.digital.Digital',
    '/enfermeria/?','mvc.controllers.enfermeria.Enfermeria',
    '/index/?','mvc.controllers.index.Index',
    '/industrial/?','mvc.controllers.industrial.Industrial',
    '/mecatronica/?','mvc.controllers.mecatronica.Mecatronica',
    '/nanotecnologia/?','mvc.controllers.nanotecnologia.Nanotecnologia',
    '/negocios/?','mvc.controllers.negocios.Negocios',
    '/ofertaeducativa/?','mvc.controllers.ofertaeducativa.Ofertaeducativa',
    '/profile/?','mvc.controllers.profile.Profile',
    '/renovables/?','mvc.controllers.renovables.Renovables',
    '/reproductiva/?','mvc.controllers.reproductiva.Reproductiva',
    '/sistemas/?','mvc.controllers.sistemas.Sistemas',
    '/terapia/?','mvc.controllers.terapia.Terapia',
    '/transparencia/?','mvc.controllers.transparencia.Transparencia',

] # COLOCAMOS LA RUTA

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()