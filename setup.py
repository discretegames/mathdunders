from distutils.core import setup
from os import read

VERSION = "0.1"

setup(
    name='mathdunders',
    version=VERSION,
    author='discretegames',
    author_email='discretizedgames@gmail.com',
    description="Decorator that adds math dunders to a class derived from a numeric type.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url='https://github.com/discretegames/mathdunders',
    packages=['mathdunders'],
    license="MIT License",
    keywords=['python', 'math', 'mathematics', 'video stream', 'camera stream', 'sockets'],
)
