from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    _add_static_views(config)
    config.scan()
    return config.make_wsgi_app()

def _add_static_views(config):
    config.add_static_view(name='css', path='herokuapp:static/css')
    config.add_static_view(name='src', path='herokuapp:static/src')
