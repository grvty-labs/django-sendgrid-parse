import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='django-sendgrid-parse',
    packages=['django_sendgrid_parse'],
    data_files=['README.md'],
    version='0.1.5',
    description='Django app to receive and save incoming email\
notification events from sendgrid to our database',
    long_description=read("README.md"),
    author='GRVTYlabs',
    author_email='daniel.ortiz@grvtylabs.com',
    url='https://github.com/letops/django-sendgrid-parse',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    install_requires=[
        'jsonfield',
    ],
)
