import re
from pathlib import Path
from setuptools import setup, find_packages

def get_version(package):
    "Return package version as listed in `__version__` in `init.py`"
    initfile = (Path(package) / "__init__.py").read_text()  # Python >= 3.5
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", initfile)[1]

def get_long_description():
    "Return the README"
    with open("README.md", "r", encoding="utf-8") as filehandle:
        long_description = filehandle.read()
    return long_description

setup(
    name='LangSegment',
    version=get_version("LangSegment"),
    packages=find_packages(),
    include_package_data=True,
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    python_requires=">=3.6",
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    install_requires=[
        "numpy >= 1.19.5",  # for Python 3.6+
        'py3langid >= 0.3.0',
    ],
    description='This is a multilingual tokenization tool that currently supports for zh/ja/en/ko, and more languages.',
    keywords=["language detection", "language identification", "langid", "langid.py","nlp","language"],
    url='https://github.com/juntaosun/LangSegment',
)