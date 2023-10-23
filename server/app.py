#!/usr/bin/env python3
import os

from flask import Flask, request, current_app, g, make_response

app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''

    status_code = 200
    headers = {}

    return make_response(response_body, status_code, headers)

#from flask import redirect

# The redirect() function is usually delivered with a "301: Moved Permanently" or "302: Found" status code. These signify that the URL for the resource on our server has been changed. Rather than torture the user with trying to find the new URL, we can redirect them to the current URL for the resource.

# redirect() is very simple: it takes one argument, the URL for the relocated resource.

# @app.route('/reginald-kenneth-dwight')
# def index():
#     return redirect('names.com/elton-john')



# or

# if you navigate to the above link, you'll notice a "404: Not Found" status code! This means that the resource does not exist for the website in question. If we want to inform users of this error in our applications, we need to use Flask's abort() function:


# from flask import abort, make_response
# ...

# @app.route('/<stage_name>')
# def get_name(stage_name):
#     match = session.query('StageName').filter(StageName.name == stage_name)[0]
#     if not match:
#         abort(404)
#     return make_response(f'<h1>{stage_name} is an existing stage name!</h1>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
