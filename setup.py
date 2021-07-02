import setuptools
from os import path
from distutils.core import setup

version = "0.2.4"

long_description = """
mathdunders provides a Python 3 decorator that automatically adds 23 math-related dunder methods to a class derived from a numeric type.

Installation:

pip install mathdunders

Usage:

from mathdunders import mathdunders

@mathdunders()
class RealNumber(float):
    pass

x = RealNumber(1) + RealNumber(2)
print(x, type(x))  # -> 3 <class '__main__.RealNumber'>
"""

setup(
    name='mathdunders',
    version=version,
    author='discretegames',
    author_email='discretizedgames@gmail.com',
    description="Decorator that adds math dunders to a class derived from a numeric type.",
    long_description=long_description,
    url='https://github.com/discretegames/mathdunders',
    py_modules=['mathdunders'],
    license="MIT License",
    keywords=['python', 'math', 'mathematics', 'dunder', 'double under', 'underscore', 'magic method', 'number']
)
