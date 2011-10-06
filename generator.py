"""Mennonite lorem ipsum generator"""

import os.path
import random
from webob import Response
from webob.dec import wsgify
from paste.httpserver import serve
from paste.fileapp import DirectoryApp

fillers = open('lists/fillers.txt').read().splitlines()
phrases = open('lists/phrases.txt').read().splitlines()
words = open('lists/words.txt').read().splitlines()

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
            parts = [random.choice(source) for source in (phrases, words, fillers, phrases, words)]
            sentence = ' '.join(parts) + '. '
            out += sentence[0].upper() + sentence[1:]
        
        out += '</p>'
    
    return Response(out)


if __name__ == '__main__':
    serve(generate_paras, host='127.0.0.1', port=8080)
