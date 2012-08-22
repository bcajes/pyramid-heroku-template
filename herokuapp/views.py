from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/index.pt')
def index(request):

    return {}

