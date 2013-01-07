# -*- coding: utf-8 -
#
# This file is part of python-dikbm-adapter released under the MIT license. 
# See the NOTICE for more information.

import os
import sys
from setuptools import setup, find_packages

from dikbm_adapter import VERSION


setup(
    name='dikbm_adapter',
    version=VERSION,
    description='DiKBM adapter to send request to web service',
    long_description=file(
        os.path.join(
            os.path.dirname(__file__),
            'README.md'
        )
    ).read(),
    author='Victor Safronovich',
    author_email='vsafronovich@gmail.com',
    license='MIT',
    url='http://github.com/suvit/python-dikbm-adapter',
    zip_safe=False,
    packages=find_packages(exclude=['docs', 'examples', 'tests']),
    install_requires=['suds',
                      'suds-passworddigest',
                      'lockfile'],
    include_package_data=True,
    entry_points={
            'console_scripts': [
                'dikbm_main = dikbm_adapter.main:main',
            ]
        }
)
