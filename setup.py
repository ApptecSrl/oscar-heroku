import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='oscar-heroku',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A simple app for integrate django-oscar with heroku and amazon S3.',
    long_description=README,
    url='https://www.apptecsrl.com/',
    author='Fabio.bocconi',
    author_email='fabio.bocconi@apptecsrl.com',
    install_requires=[
        'django-oscar==1.5.1',
        'pycountry',
        'dj-database-url==0.4.1',
        'gunicorn==19.6.0',
        'psycopg2==2.6.2',
        'whitenoise==3.2',
        'django-storages',
        'boto3',
        'raven'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
