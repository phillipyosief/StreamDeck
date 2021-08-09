import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="StreamDeck-Client-Test",
    version="0.0.2-alpha",
    description="Use any device which can run python as a streamdeck like a Raspberry Pi",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/philliphqs/StreamDeck",
    author="philliphqs",
    author_email="contact@hqsartworks.me",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["requests", "dearpygui"],
)
