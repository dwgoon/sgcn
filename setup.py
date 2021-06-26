
from setuptools import setup, find_packages

setup(
    name='sgcn',
    version="0.0.1",
    description='Steganography of Complex Networks',
    author='Daewon Lee',
    author_email='daewon4you@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'pandas',
        'networkx',
        'bitstring',
        'tqdm'
    ]
)
