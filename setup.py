from setuptools import setup, find_packages

base_packages = []

test_packages = [
    "pytest>=6.2.1",
    "black>=20.8b1",
    "flake8>=3.8.4",
]

util_packages = ["jupyterlab>=3.0.1", "pre-commit>=2.9.3"]

dev_packages = test_packages + util_packages

setup(
    name="clumper",
    version="0.1.1",
    packages=find_packages(),
    extras_required={"dev": dev_packages, "test": test_packages},
)
