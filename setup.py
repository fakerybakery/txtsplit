from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="txtsplit",
    version="1.0.0",
    author="mrfakename",
    author_email="me@mrfake.name",
    description="A simple text splitter based on Tortoise for use in text-to-speech applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fakerybakery/txtsplit",
    packages=["txtsplit"],
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
    ],
    python_requires=">=3.9",
    platforms=["Any"],
    license="Apache 2.0"
)