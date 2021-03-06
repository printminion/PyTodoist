#!/usr/bin/env python

from distutils.core import setup

setup(name = 'pytodoist',
      version = '0.1dev',
      license = 'MIT',
      description = 'A python wrapper for the Todoist API.',
      long_description = open('README').read(),
      author = 'Gary Blackwood',
      author_email = 'gary@garyblackwood.co.uk',
      url = 'http://www.github.com/Garee/PyTodoist',
      packages = ['pytodoist'],
      install_requires = ['requests'],)
