from distutils.core import setup
from setuptools import find_packages
import re

with open("readme.md", "r") as f:
    long_description = f.read()

VERSIONFILE = "statannotations/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", verstrline, re.M)
if match:
    version = match.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
    name="statannotations",
    version=version,
    author="Florian Charlier",
    author_email="florian.charlier@cascliniques.be",
    description=("add statistical annotations on existing box or barplots "
                 "generated by seaborn, based on statannot"),
    license="MIT License",
    license_file="LICENSE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trevismd/statannotations",
    packages=find_packages(exclude=("tests", "doc")),
    include_package_data=True,  # For documentation
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=open("requirements.txt").readlines(),
    python_requires='>=3.5',
)
