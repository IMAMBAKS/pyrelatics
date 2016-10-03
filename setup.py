from distutils.core import setup

setup(
    name='pyrelatics',
    packages=['pyrelatics'],
    version='0.21',
    description='API for Relatics connections',
    install_requires=['beautifulsoup4>=4', 'suds-jurko==0.6'],
    author='Rashied Imambaks',
    author_email='r@imambaks.nl',
    url='https://github.com/IMAMBAKS/pyrelatics',
    license='MIT',
    keywords=['relatics', 'SOAP', 'API', 'DB'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
