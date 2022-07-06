"""Setup the SDeconv submodule"""
import sys
import os
from numpy.distutils.misc_util import Configuration

from sdeconv._build_utils import cythonize_extensions


__version__ = '1.0.1'


def configuration(parent_package='', top_path=None):
    """Submodule configuration

    Parameters
    ----------
    parent_package: str
        Name of the parent package
    top_path: str
        Path of the top module

    """
    libraries = []
    if os.name == 'posix':
        libraries.append('m')

    config = Configuration('sdeconv', parent_package, top_path)

    # submodules with build utilities
    config.add_subpackage('__check_build')
    config.add_subpackage('_build_utils')

    # submodules which have their own setup.py
    config.add_subpackage('deconv')
    config.add_subpackage('psfs')

    # Skip cythonization as we do not want to include the generated
    # C/C++ files in the release tarballs as they are not necessarily
    # forward compatible with future versions of Python for instance.
    if 'sdist' not in sys.argv:
        cythonize_extensions(top_path, config)

    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
