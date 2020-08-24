#! /usr/bin/env python

#
# Copyright 2020 Spotify AB
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os

from setuptools import find_packages
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

REQUIRED_PACKAGES = [
    'apache_beam[gcp]',
    'tensorflow',
    'matplotlib',
    'fire',
    'pandas',
    'tqdm'
]

setup(
    name="rips",
    version='0.0.1',
    description="KDD 2020 RIPS",
    url="",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ],
    zip_safe=False,
    install_requires=REQUIRED_PACKAGES,
)
