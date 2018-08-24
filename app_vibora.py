from vibora import Vibora, Request, Response
from vibora.responses import JsonResponse
from vibora.router import RouterStrategy
from vibora.static import StaticHandler

app = Vibora(
    template_dirs=['./templates',],
    router_strategy=RouterStrategy.CLONE,
    static=StaticHandler(
        paths=['./static'],
        url_prefix='/static',
        max_cache_size=1 * 1024 * 1024
    )
)


@app.route('/', methods=['POST', "GET"])
async def home(request: Request):
    print(request.method)
    if request.method == 'POST':
        print(await request.form())
    else:
        for x in request.args: print(x)

    return await app.render("index.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9999)
