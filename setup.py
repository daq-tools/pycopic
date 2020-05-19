# -*- coding: utf-8 -*-
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst'), encoding="utf-8").read()

setup(name='pycopic',
      version='0.0.0',
      description='An attempt to mix Pycom\'s "pycoproc" with "pypic" in order to '
                  'control the PIC through the serial interface',
      long_description=README,
      license="GPL 3",
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: GNU General Public License v3",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "Topic :: Communications",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Networking :: Monitoring",
        "Topic :: Utilities",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS"
        ],
      author='Andreas Motl',
      author_email='andreas.motl@terkin.org',
      url='https://github.com/daq-tools/pycopic',
      keywords='pycom pycoproc pypic',
      py_modules=[
          'pycoproc',
          'pypic',
          'pycopic',
      ],
      zip_safe=False,
      install_requires=[
          'pyserial==3.4',
          'mock==4.0.2',
          #'esp32-machine-emulator==1.1.3',
      ],
      entry_points={
          'console_scripts': [
              'pycopic = pycopic:main',
          ],
      },
)
