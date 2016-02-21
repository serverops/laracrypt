# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__version__ = '1.0.0'

setup(name='laracrypt',
      version=__version__,
      description="Laravel-compatible two-way encryption",
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Operating System :: POSIX",
          "Environment :: Console",
          "Programming Language :: Python",
          "Topic :: Internet :: Proxy Servers",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: System :: Systems Administration"
      ],
      keywords=['encrypt', 'encryption', 'laravel'],
      author='Chris Fidao',
      author_email='chris@serverops.io',
      url='https://github.com/serverops/laracrypt',
      license='MIT',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      install_requires=['pycrypto', 'phpserialize'],
      tests_require=['nose'],
      test_suite='nose.collector'
)
