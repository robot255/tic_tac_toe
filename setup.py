import io

from setuptools import setup, find_packages

try:
    long_description = io.open("README.rst", encoding="utf-8").read()
except IOError:
    long_description = "See https://github.com/robot255/tic_tac_toe/blob/master/README.txt"

setup(
    name="tic_tac_toe",
    version="0.0.1",
    url="https://github.com/robot255/tic_tac_toe",
    author="jason s",
    author_email="jmgstrach@gmail.com",
    description="A fun little tic tac toe program",
    packages=find_packages(),
    long_description=long_description,
    install_requires=['parameterized']
)
