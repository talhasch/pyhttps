# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='pyhttps',
      version='0.0.1',
      author='Talha Buğra Bulut',
      author_email='talhabugrabulut@gmail.com',
      url='https://github.com/talhasch/pyhttps',
      py_modules=['pyhttps'],
      entry_points={
          "console_scripts": [
              "pyhttps = pyhttps:main"
          ]
      }
      )
