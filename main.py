# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask
from flask import request  # https://2.python-requests.org/en/master/#


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
# https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
app = Flask(__name__)


konstant = dict()


@app.route('/')
def hello():
    global konstant
    # Return a friendly HTTP greeting
    return '<h1>Hello Wally!</h1>' + ' ' + konstant

def foo():
    return "<br><b>foo</b>"

@app.route('/bar')
def bar():
    return "<h2> where is Bar?</h2>"

@app.route('/testPost', methods=['POST'])
def testPost():
    global  konstant
    konstant = request.form['key1']
    return "testPost"



if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
# python-docs-samples/appengine/standard_python37/hello_world