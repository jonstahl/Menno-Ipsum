"""Mennonite lorem ipsum generator"""

import os.path
import random
from webob import Response
from webob.dec import wsgify
from paste.httpserver import serve
from paste.fileapp import DirectoryApp
from produce import build_sentence

static = DirectoryApp(os.path.dirname(__file__))


@wsgify
def generate_paras(request):
    if request.path != '/generator':
        if request.path == '/':
            request.path_info = '/index.html'
        return static
    
    paras = int(request.GET.get('p', 4))
    sentence_max = int(request.GET.get('smax', 9))
    sentence_min = int(request.GET.get('smin', 5))
    
    out = ''
    for i in range(paras):
        out += '<p>'
        sentence_per_para = random.randint(sentence_min, sentence_max)
        for j in range(sentence_per_para):
            out += build_sentence() + ' '
        out += '</p>'
    
    return Response(out)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    serve(generate_paras, host='0.0.0.0', port=port)
