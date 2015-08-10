from distutils.core import setup
from setuptools import setup, find_packages

setup(
  name = 'relatics_api',
  packages = ['relatics_api'], 
  version = '0.1.0',
  description = 'Soap API for Relatics',
  author = 'Rashied Imambaks',
  author_email = 'r@imambaks.nl',
  url = 'https://github.com/IMAMBAKS/SOAP__Relatics',
  license = 'MIT',
  keywords = ['relatics', 'SOAP'], 
  classifiers = [

	  'Development Status :: 5 - Production/Stable',
	  'Intended Audience :: Developers',
	  'Natural Language :: English',
	  'License :: OSI Approved :: MIT License',
	  'Operating System :: OS Independent',
	  'Programming Language :: Python',
	  'Programming Language :: Python :: 2.7',
	  'Programming Language :: Python :: 3',
	  'Programming Language :: Python :: 3.3',
	  'Topic :: Software Development :: Libraries :: Python Modules',
  ],
  packages=find_packages(exclude=['tests*']),
)