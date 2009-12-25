#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
obspy.seishub installer

@copyright: The ObsPy Development Team (devs@obspy.org)
@license: GNU Lesser General Public License, Version 3 (LGPLv3)
"""

from setuptools import setup, find_packages


VERSION = '0.2.0'


setup(
    name='obspy.seishub',
    version=VERSION,
    description="SeisHub database client for ObsPy.",
    long_description="""
    obspy.seishub - SeisHub database client for ObsPy.

    For more information visit http://www.obspy.org.
    """,
    url='http://www.obspy.org',
    author='The ObsPy Development Team',
    author_email='devs@obspy.org',
    classifiers=[],
    keywords=['ObsPy', 'seismology', 'SeisHub'],
    license='LGPLv3',
    packages=find_packages(),
    namespace_packages=['obspy'],
    zip_safe=True,
    install_requires=[
        'setuptools',
        'obspy.core>0.2.1',
        'obspy.mseed>0.2.1',
        'lxml',
        'matplotlib',
    ],
    download_url="https://svn.geophysik.uni-muenchen.de" + \
        "/svn/obspy/obspy.seishub/trunk#egg=obspy.seishub-dev",
    platforms=['any'],
    test_suite="obspy.seishub.tests.suite",
    include_package_data=True,
)
