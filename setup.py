import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "stop-it",
    version = "0.0.1",
    author = "Teresa Ingram",
    author_email = "tee.in.grams@gmail.com",
    description = ("An browser extension to stop sexual harassment online"),
    license = "Apache 2.0",
    url = "https://github.com/malteserteresa/stop-it",
    packages=['src', 'tests'],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: :: Apache License",
    ],
)