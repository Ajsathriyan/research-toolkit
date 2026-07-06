# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 18:31:36 2026

@author: AJITH
"""

from setuptools import setup, find_packages

setup(
    name="research-toolkit",
    version="1.0.0",
    author="AJITH",
    author_email="makumar735@gmail.com",
    description="A Python toolkit for statistical analysis, visualization, and reporting for research.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Ajsathriyan/research-toolkit.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy>=1.22",
        "pandas>=1.5",
        "scipy>=1.10",
        "matplotlib>=3.7",
        "openpyxl>=3.1",
    ],
    python_requires=">=3.9",
    license="MIT",
    keywords=[
        "research",
        "statistics",
        "data analysis",
        "visualization",
        "medical physics",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
    ],
)