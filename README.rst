.. image:: https://circleci.com/gh/RealSalmon/python-namesake.svg?style=shield
    :target: https://circleci.com/gh/RealSalmon/python-namesake
    
namesake
========

namesake is a dead simple memorable name generator for Python.

Python versions 2.6, 2.7, 3.3, 3.4, and 3.5 are supported.


Installation
------------

::

    pip install namesake

Usage
-----

::

    #!/usr/bin/env python
    
    from namesake import getname
    print(getname())

A command line version is also included::

    #!/usr/bin/env bash
    
    namesake-name
