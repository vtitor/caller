from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="caller",
    version="0.0.2",
    description="Set a Python property using a function call",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Victor Titor",
    author_email="vtitor.edumix@gmail.com",
    url="https://github.com/vtitor/caller",
    packages=["caller"],
    tests_require=["pytest"],
    extras_require={"dev": ["pre-commit", "black"]},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
    ],
)
