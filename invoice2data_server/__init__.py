import json
import tempfile
import datetime
from functools import partial

import asyncio

from aiohttp import (
    web,
    MultipartReader
)
from invoice2data import extract_data


def default_json(obj):
    if isinstance(obj, datetime.datetime):
        return str(obj)
    raise TypeError('Unable to serialize {!r}'.format(obj))


async def handle_index(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


async def handle_file_post(request):
    form = await request.post()
    raw_data = form['file'].file.read()
    with tempfile.NamedTemporaryFile() as tmp_file:
        tmp_file.write(raw_data)
        result = extract_data(tmp_file.name)
        if result:
            response = web.json_response(
                {'success': True, 'result': result},
                dumps=request.app['dumps']
            )
        else:
            response = web.json_response({'success': False})
    return response


def setup_routes(app):
    app.router.add_routes(
        [
            web.get('/', handle_index, name='index'),
            web.post('/', handle_file_post, name='index'),
        ]
    )


async def init_app():
    app = web.Application(client_max_size=10*1024**2)

    setup_routes(app)
    app['dumps'] = partial(json.dumps, default=default_json)
    return app


def serve():
    app = init_app()
    loop = asyncio.get_event_loop()
    loop.create_task(web.run_app(app))


if __name__ == '__main__':
    serve()
