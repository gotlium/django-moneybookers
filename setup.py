from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='django-moneybookers',
      version=version,
      url='https://github.com/mikery/django-moneybookers',
      packages=find_packages(exclude=['examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      )
