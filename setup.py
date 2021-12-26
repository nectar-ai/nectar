import os

from importlib.machinery import SourceFileLoader
from setuptools import setup, find_packages

version = (
    SourceFileLoader("nectar.version", os.path.join("nectar", "version.py")).load_module().VERSION
)

setup(
    name="nectar",
    version=version,
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        nectar=nectar.cli:cli
    """
)