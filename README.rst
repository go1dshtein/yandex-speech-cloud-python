Yandex Speech Cloud Tools
=========================

It is open source tools for text2speech and speech2text transformations
based on `Yandex SpeechKit
Cloud <https://tech.yandex.ru/speechkit/cloud/>`__.

Usage
-----

| First of all you need to get key for API from Yandex.
| Save it to file ``~/.ysckey``.

TTS
~~~

Simple usage:

::

    yandex-speech-cloud-python: user$ ./bin/tts
    здравствуй, мир!
    ^D
    yandex-speech-cloud-python: user$

You can change speaker and emotions:

::

    yandex-speech-cloud-python: user$ ./bin/tts -s zahar -e evil
    я очень злой мужик!
    ^D
    yandex-speech-cloud-python: user$

Instead of playing record you can save it to file:

::

    yandex-speech-cloud-python: user$ ./bin/tts -e mixed >mixed.wav
    какие-то непонятные эмоции я сейчас испытываю
    ^D
    yandex-speech-cloud-python: user$

ASR
~~~

Basic mode records your voice and sends it to yandex:

::

    yandex-speech-cloud-python: user$ ./bin/asr
    2014-11-12 00:37:33,915: INFO: ysc.audio: press enter to stop

    1: Как пройти в библиотеку
    yandex-speech-cloud-python: user$

You can choose topic:

::

    yandex-speech-cloud-python: user$ ./bin/asr -t maps
    2014-11-12 00:44:38,875: INFO: ysc.audio: press enter to stop

    0.66: Бэйкер стрит 221 б
    0: Бейкер стрит 221 б
    yandex-speech-cloud-python: user$

And source:

::

    yandex-speech-cloud-python: user$ cat ~/numbers.wav | ./bin/asr 
    1: 1 2 3 4 5
    yandex-speech-cloud-python: user$

