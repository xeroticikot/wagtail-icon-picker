import io
import re
import sys
import os
from os import path
from setuptools import setup, find_packages


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()


install_requires = ["wagtail"]

tests_require = ["pytest-django", "wagtail-factories", "pytest"]

# Convert markdown to rst
# try:
#     from pypandoc import convert_file
#     long_description = convert_file("README.md", "rst")
# except:  # NOQA
#     long_description = ""

version = ''
with io.open('wagtail_icon_picker/__init__.py', 'r', encoding='utf8') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)


setup(
    version=version,
    name="wagtail-icon-picker",
    description="Wagtail CMS icon picker including Bootstrap Icons, Boxicons, Icofont & Font awesome libraries.",
    long_description='',
    author="Mahmud Abdur Rahman",
    author_email="clanlord.ikot@gmail.com",
    url="https://github.com/xeroticikot/wagtail-icon-picker",
    project_urls={
        "Bug Tracker": "https://github.com/xeroticikot/wagtail-icon-picker/issues",
    },
    packages=find_packages(
        exclude=("*.tests", "*.tests.*", "tests.*", "tests", "example*")
    ),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
    tests_require=tests_require,
    extras_require={"test": tests_require},
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
    ],
    setup_requires=["setuptools_scm", "pytest-runner"],
    python_requires=">=3.6",
)
