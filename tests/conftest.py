# Copyright (C) 2018-2020  Yannick Jadoul
#
# This file is part of Parselmouth.
#
# Parselmouth is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Parselmouth is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Parselmouth.  If not, see <http://www.gnu.org/licenses/>

import pytest

import os
import sys

if '' not in sys.path:
	sys.path.insert(2, '')


def pytest_addoption(parser):
	parser.addoption('--run-praat-tests', action="store_true", default=False, help="run Praat tests")


def pytest_collection_modifyitems(config, items):
	praat_tests = bool(config.getoption('--run-praat-tests'))
	if not praat_tests:
		skip_marker = pytest.mark.skip(reason="need --run-praat-tests option to run")
		for item in items:
			if 'praat_test' in item.keywords:
				item.add_marker(skip_marker)


class Resources(object):
	def __init__(self, base_path):
		self.base_path = base_path
	
	def __getitem__(self, file_name):
		return os.path.join(self.base_path, "data", file_name)


@pytest.fixture(scope="module")
def resources(request):
	return Resources(request.fspath.dirname)


from resource_fixtures import *
