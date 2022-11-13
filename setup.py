from setuptools import find_packages, setup

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="materials_propellant",
    version="1.0.1",
    description="Librirary with materials and propellant for peuro",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/LaArkadiy/peuro_lab1',
    author=["LaArkady", "DaMikhaylovv"],
    license="MIT",
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Natural Language :: Russian",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[]
)