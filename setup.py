# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from version import version

setup(name='pyhttps',
      description='Simple python https server creator',
      keywords=['https', 'server'],
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
