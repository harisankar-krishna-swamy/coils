import setuptools

with open("../README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycoils",
    version="1.6.0",
    author="Harisankar Krishna Swamy",
    author_email="harisankar.krishna@outlook.com",
    description="A Python datastructure library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/harisankar-krishna-swamy-code/coils",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)