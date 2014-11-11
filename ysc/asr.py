import os
import asyncio
import aiohttp
import logging
from urllib.parse import urlencode
import xml.etree.ElementTree as ET


logger = logging.getLogger(__name__)


@asyncio.coroutine
def asr(loop, inputstream, outputstream, params):
    url = "https://asr.yandex.net/asr_xml?"
    url += urlencode(params)

    response = yield from aiohttp.request(
        "POST", url, headers={'Content-Type': 'audio/x-wav'},
        chunked=True, data=inputstream, loop=loop)
    logger.debug("asr: response: \n%s", response)
    body = yield from response.read()
    logger.debug("asr: body: \n%s", body)

    root = ET.fromstring(body.decode("utf8"))
    for child in root:
        outputstream.write("{}: {}\n".format(
            child.attrib["confidence"], child.text))
