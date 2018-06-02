import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycurrency-convertor",
    version="0.0.1",
    author="Vaibhav Singh",
    author_email="author@vaibhavsingh97.com",
    description="A python package to convert currencyt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vaibhavsingh97/pycurrency-convertor",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)