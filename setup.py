import setuptools
import os

# Get the long description from the README file
with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="devicemonitor",
    version="0.0.1",
    author="Gabriel Domanowski",
    author_email="gabrieldomanowski@gmail.com",
    description="A package for monitoring devices for the recruitment task",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/sagbot/pydev",
    license='UNLICENSED',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: UNLICENSED",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    package_dir={"": "devicemonitor"},
    packages=setuptools.find_packages("devicemonitor")
)

