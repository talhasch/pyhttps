# -*- coding: utf-8 -*-

from setuptools import setup

from version import version

setup(name='pyhttps',
      version=version,
      author='Talha Buğra Bulut',
      author_email='talhabugrabulut@gmail.com',
      url='https://github.com/talhasch/pyhttps',
      py_modules=['pyhttps', 'version'],
      entry_points={
          "console_scripts": [
              "pyhttps = pyhttps:main"
          ]
      }
      )
