"""
Created on Sep 22, 2011

@author: Vishal Rana
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*

from setuptools import setup
 
setup(
    name="stocktik",
    version="0.1",
    description="A bunch of technical indicators and overlays.",
    author="Vishal Rana",
    author_email="vishal@qwata.com",
    url="http://github.com/vishr/stocktik",
    packages=["stocktik"],
    install_requires=["numpy"],
    platforms=["any"],
    license="GPL"
)
