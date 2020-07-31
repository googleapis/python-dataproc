# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import absolute_import
import os

import nox


@nox.session
def default(session):
    return unit(session)


@nox.session(python=['2.7', '3.5', '3.6', '3.7'])
def unit(session):
    """Run the unit test suite."""

    # Install all test dependencies, then install this package in-place.
    session.install('pytest', 'mock')
    session.install('-e', '.')

    # Run py.test against the unit tests.
    session.run('py.test', '--quiet', os.path.join('tests', 'unit'))


@nox.session(python=['2.7', '3.7'])
def system(session):
    """Run the system test suite."""

    # Sanity check: Only run system tests if the environment variable is set.
    if not os.environ.get('GOOGLE_APPLICATION_CREDENTIALS', ''):
        session.skip('Credentials must be set via environment variable.')

    # Install all test dependencies, then install this package in-place.
    session.install('pytest')
    session.install('-e', '.')

    # Run py.test against the unit tests.
    session.run(
        'py.test',
        '--quiet',
        os.path.join('tests', 'system'),
        *session.posargs
    )


@nox.session
def lint_setup_py(session):
    """Verify that setup.py is valid (including RST check)."""
    session.install('docutils', 'pygments')
    session.run(
        'python', 'setup.py', 'check', '--restructuredtext', '--strict')