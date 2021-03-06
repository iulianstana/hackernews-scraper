from setuptools import setup, find_packages

import codecs
import os
import re

root_dir = os.path.abspath(os.path.dirname(__file__))
PACKAGE = 'hackernews_scraper'

def get_version(package_name):
    version_re = re.compile(r"^__version__ = [\"']([\w_.-]+)[\"']$")
    package_components = package_name.split('.')
    init_path = os.path.join(root_dir, *(package_components + ['__init__.py']))
    with codecs.open(init_path, 'r', 'utf-8') as f:
        for line in f:
            match = version_re.match(line[:-1])
            if match:
                return match.groups()[0]
    raise Exception("No package version found!")

setup(name=PACKAGE,
      description='Python library for retrieving comments and stories from HackerNews',
      packages=find_packages(),
      version=get_version(PACKAGE),
      install_requires=['requests'],
      url='https://github.com/NiGhTTraX/hackernews-scraper',
      license='MIT',
      platforms='any',
      tests_require=['nose', 'factory_boy', 'httpretty'],
      )
