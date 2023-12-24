from setuptools import setup

with open("VERSION") as f:
    version = f.read().strip()

setup(
    name="pdf_parser",
    version=version,
    packages=["pdf_parser"],
)
