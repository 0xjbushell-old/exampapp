import sys
sys.path.append('/opt/exampapp/app')
from proc import connect

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    response = connect()
    return response
