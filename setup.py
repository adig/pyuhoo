from setuptools import setup

setup(
    name="pyuhoo",
    version="0.0.1",
    description="Python API for talking to uHoo consumer API",
    long_description=open("README.md").read(),
    url="https://github.com/csacca/pyuhoo",
    author="Christopher Sacca",
    author_email="csacca@csacca.net",
    license="MIT",
    packages=["pyuhoo"],
    install_requires=["requests"],
)