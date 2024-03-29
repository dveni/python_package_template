#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
from distutils.core import setup

# Package meta-data.
NAME = "package_name"
DESCRIPTION = "My short description for my project."
URL = "https://github.com/dveni/python_package_template"
EMAIL = "me@example.com"
AUTHOR = "Daniel Vera Nieto"
REQUIRES_PYTHON = ">=3.12.0"
VERSION = None

# What packages are required for this module to be executed?
REQUIRED = [
    "jsonargparse",
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
    "test": ["pytest"],
    "development": ["pre-commit"],
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


setup(
    name=NAME,
    version=about["__version__"],
    author=AUTHOR,
    author_email=EMAIL,
    packages=["package_name"],
    scripts=["scripts/example_script.py"],
    url=URL,
    license="LICENSE",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    entry_points="""
        [console_scripts]
        mypackage = package_name.module:print_hello
        """,
)
