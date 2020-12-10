import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CMFluid",
    version="0.0.1",
    author="Paul Tembo, Junyi Guo, Matthew Hawes, Jack Scudder , Arthur Young",
    author_email="",
    description="cs207 Final Project and implementation of Auto Differentiaion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cache-Money404/cs107-FinalProject",
    packages=setuptools.find_packages(),
    install_requires=['numpy==1.16.3'], 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)