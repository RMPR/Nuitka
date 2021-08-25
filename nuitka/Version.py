#     Copyright 2021, Kay Hayen, mailto:kay.hayen@gmail.com
#
#     Part of "Nuitka", an optimizing Python compiler that is compatible and
#     integrates with CPython, but also works on its own.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
""" Nuitka version related stuff.

"""

version_string = """\
Nuitka V0.6.16.4
Copyright (C) 2021 Kay Hayen."""


def getNuitkaVersion():
    """Return Nuitka version as a string.

    This should not be used for >= comparisons directly.
    """
    return version_string.split()[1][1:]


def getNuitkaVersionYear():
    """The year of Nuitka copyright for use in generations."""

    return int(version_string.split()[4])


def getCommercialVersion():
    """Return Nuitka commercial version if installed."""
    try:
        from nuitka.tools.commercial import Version
    except ImportError:
        return None
    else:
        return Version.__version__
