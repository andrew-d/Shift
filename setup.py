#!/usr/bin/env python

from setuptools import setup

setup(name='Shift',
      version='0.0.1',
      description='A generic template library for Python',
      author='Andrew Dunham',
      url='http://github.com/andrew-d/Shift',
      license='Apache',
      platforms='any',
      zip_safe=False,
      packages=['shift'],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      test_suite = 'shift.tests.suite',
     )

