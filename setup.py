import os
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='django-sendgrid-parse',
    version='0.4.3',
    description='Django app to receive and save incoming email\
notification events from sendgrid to our database',
    long_description=readme,
    # long_description=read("README.md"),
    author='GRVTY',
    author_email='daniel.ortiz@grvtylabs.com',
    url='https://github.com/grvty-labs/django-sendgrid-parse',
    packages=find_packages(),
    # packages=['django_sendgrid_parse'],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'jsonfield',
        'sendgrid',
    ],
)
