
from setuptools import setup, find_packages

setup(
    name='sgcn',
    version="0.0.1",
    description='Steganography for Complex Networks',
    author='Daewon Lee',
    author_email='daewon4you@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'networkx',          
    ]
)
