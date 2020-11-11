import setuptools
import pycoils

with open("../README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycoils",
    version=pycoils.version,
    author="Harisankar Krishna Swamy",
    license='Apache2',
    author_email="harisankar.krishna@outlook.com",
    description="A Python datastructure library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/harisankar-krishna-swamy/coils.git",
    packages=setuptools.find_packages(),
    python_requires='>=3.7.4, <4',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)