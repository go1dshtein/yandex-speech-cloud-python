import os
import asyncio
import aiohttp
import logging
from urllib.parse import urlencode


logger = logging.getLogger(__name__)


@asyncio.coroutine
def tts(loop, inputstream, outputstream, params):
    params["text"] = inputstream.read()

    url = "https://tts.voicetech.yandex.net/generate?"
    url += urlencode(params)

    response = yield from aiohttp.request("GET", url, loop=loop)
    body = yield from response.read()

    outputstream.write(body)
