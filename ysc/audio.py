import io
import wave
import pyaudio
import logging
import threading


logger = logging.getLogger(__name__)


def record():
    chunk = 1024
    format = pyaudio.paInt16
    channels = 2
    sampwidth = 2
    rate = 16000

    buffer = io.BytesIO()
    wf = wave.open(buffer, 'wb')
    wf.setframerate(rate)
    wf.setsampwidth(sampwidth)
    wf.setnchannels(channels)

    logger.debug("record: framerate: %s", rate)
    logger.debug("record: sampwidth: %s", sampwidth)
    logger.debug("record: channels: %s", channels)

    pa = pyaudio.PyAudio()

    def callback(indata, framecount, timeinfo, status):
        wf.writeframes(indata)
        return (None, pyaudio.paContinue)

    stream = pa.open(
        format=format, channels=channels,
        rate=rate, input=True, stream_callback=callback)

    logger.info("press enter to stop")
    input("")

    stream.stop_stream()
    stream.close()

    logger.info("record: buffer size: %s", len(buffer.getvalue()))
    buffer.seek(0)
    return buffer


def play(outputstream):
    wf = wave.open(outputstream, 'rb')

    pa = pyaudio.PyAudio()
    et = threading.Event()

    def callback(indata, framecount, timeinfo, status):
        outdata = wf.readframes(framecount)
        if wf.getnchannels() * wf.getsampwidth() * framecount != len(outdata):
            et.set()
        return (outdata, pyaudio.paContinue)

    stream = pa.open(
        format=pyaudio.paInt16, channels=wf.getnchannels(),
        rate=wf.getframerate(), output=True, stream_callback=callback)

    et.wait()

    stream.stop_stream()
    stream.close()
