#!/usr/bin/env python3
from werkzeug.wrappers import Request, Respose

@Request.application
def application(request):
    print (f"This web server is running at {request.remote_addr}")
    return Respose('A WSGI generated this response!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple("localhost", 8080, application= application)
