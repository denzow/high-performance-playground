import jinja2
import jinja2_sanic

from sanic import Sanic
from sanic.response import json, HTTPResponse
from sanic_session import Session, InMemorySessionInterface

app = Sanic()
session = Session(app, interface=InMemorySessionInterface())
jinja2_sanic.setup(
    app,
    loader=jinja2.FileSystemLoader('./templates', encoding='utf8')
)


@app.route('/favicon.ico')
async def favicon(request):
    return HTTPResponse()


@app.route('/')
async def get(request):
    if not request['session'].get('foo'):
        request['session']['foo'] = 0

    request['session']['foo'] += 1
    return jinja2_sanic.render_template("index.html", request, {'name': 'spam', 'foo': request['session']['foo']})


@app.route('/', methods=['POST'])
async def post(request):
    print(request.form['a'])
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, workers=4, access_log=True)
