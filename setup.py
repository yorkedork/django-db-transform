from setuptools import setup, find_packages
import os

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-db-transform",
    version = "0.1",
    author = "Thom Linton",
    author_email = "thom.linton@gmail.com",
    description = "A Django microframework which provides tools to build a declarative-style data transformation library",
    license = "BSD",
    keywords = "",
    url = "http://github.com/yorkedork/django-db-transform/tree/master",
    packages=find_packages(),
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
    ],
    package_data={
    },
)
