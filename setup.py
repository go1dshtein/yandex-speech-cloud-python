#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if os.path.exists('README.rst'):
    long_description = open('README.rst').read()
else:
    long_description = "Yandex Speech Cloud Tools"

setup(name='yandex-speech-cloud',
      version='0.1',
      description='Yandex Speech Cloud Tools',
      long_description=long_description,
      author='Kirill Goldshtein',
      author_email='goldshtein.kirill@gmail.com',
      url='https://github.com/go1dshtein/yandex-speech-cloud-python',
      packages=['ysc'],
      requires=['aiohttp', 'pyaudio'],
      install_requires=['aiohttp', 'pyaudio'],
      scripts=['bin/tts', 'bin/asr'],
      license='GPLv2',
      classifiers=['Intended Audience :: Developers',
                   'Topic :: Software Development :: Libraries',
                   'Development Status :: 3 - Alpha',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3.4'])
