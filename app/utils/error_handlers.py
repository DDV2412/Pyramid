from pyramid.view import notfound_view_config, exception_view_config
from pyramid.response import Response


@notfound_view_config(renderer='json')
def not_found(request):
    return Response(json={'error': 'Not Found', 'message': 'The requested resource was not found.'}, status=404)


@exception_view_config(renderer='json')
def internal_server_error(request):
    return Response(json={'error': 'Internal Server Error', 'message': 'An internal server error occurred.'}, status=500)

