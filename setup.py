from setuptools import setup
from setuptools import find_packages

long_description = """
# dotosc
"""

required = [
    "bleak",
    "numpy",
    "python-osc"
]

setup(
    name="dotosc",
    version="0.0.1",
    author="Jacob Hart",
    url="https://github.com/jdchart/dotoscc",
    license="GLPv3+",
    author_email="jacob.dchart@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="",
    install_requires=required,
    packages=find_packages()
)