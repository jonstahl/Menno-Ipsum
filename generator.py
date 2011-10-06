from webob import Request, Response
from paste.httpserver import serve


def generate_paras(environ, start_response):
    request = Request(environ)
    return Response('')(environ, start_response)


if __name__ == '__main__':
    serve(generate_paras, host='127.0.0.1', port=8080)
