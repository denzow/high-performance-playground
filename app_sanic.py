from sanic import Sanic
from sanic.response import json

app = Sanic()


@app.route('/')
async def get(request):
    return json({'hello': 'world'})


@app.route('/', methods=['POST'])
async def post(request):
    print(request.form)
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
