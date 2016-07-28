import os
from setuptools import setup


with open('README.md') as file_readme:
    readme = file_readme.read()

setup(
    name='django-sendgrid-parse',
    packages=['django_sendgrid_parse'],
    data_files=['README.md'],
    version='0.1.5',
    description='Django app to receive and save incoming email\
notification events from sendgrid to our database',
    long_description=readme,
    packages=find_packages(),
    author='GRVTYlabs',
    author_email='daniel.ortiz@grvtylabs.com',
    url='https://github.com/letops/django-sendgrid-parse',
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
    ],
)
