# coding=utf-8
"""Python Ring Door Bell setup script."""
from setuptools import setup

_VERSION = '0.2.4'


def readme():
    with open('README.rst') as desc:
        return desc.read()


setup(
    name='ring_doorbell',
    packages=['ring_doorbell'],
    version=_VERSION,
    description='A Python library to communicate with Ring' +
                ' Door Bell (https://ring.com/)',
    long_description=readme(),
    author='Marcelo Moreira de Mello',
    author_email='tchello.mello@gmail.com',
    url='https://github.com/tchellomello/python-ring-doorbell',
    license='LGPLv3+',
    include_package_data=True,
    install_requires=['requests', 'pytz'],
    test_suite='tests',
    keywords=[
        'ring',
        'door bell',
        'home automation',
        ],
    classifiers=[
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ' +
        'GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
)
