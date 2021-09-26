"""
    Digitex Rest Trading API
"""


from setuptools import setup, find_packages

NAME = "digitex-rest-python"
VERSION = "0.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "urllib3 >= 1.26.7",
     "python-dateutil",
    ]

setup(
    name=NAME,
    version=VERSION,
    description="Digitex Python REST client",
    author="Sergiy Pavlyuk",
    author_email="spavlyuk@digitex.io",
    url="",
    keywords=["Digitex Python REST client"],
    python_requires=">=3.8",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT License",
    long_description=""" """
)
