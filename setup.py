from setuptools import setup, find_packages

setup(
    name="nectar",
    version="0.0.1-alpha",
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        nectar=nectar.cli:cli
    """
)