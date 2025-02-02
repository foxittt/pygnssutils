"""
Created on 26 May 2022

@author: semuadmin
"""
import setuptools

from pygnssutils import version as VERSION

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygnssutils",
    version=VERSION,
    author="semuadmin",
    author_email="semuadmin@semuconsulting.com",
    description="UBX Protocol Parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/semuconsulting/pygnssutils",
    packages=setuptools.find_packages(exclude=["tests", "examples", "docs"]),
    install_requires=[
        "pyubx2>=1.2.11",
        "pynmeagps>=1.0.13",
        "pyrtcm>=0.2.6",
        "pyserial>=3.4",
    ],
    entry_points={
        "console_scripts": [
            "gnssdump = pygnssutils.gnssdump:main",
            "gnssserver = pygnssutils.gnssserver:main",
        ]
    },
    license="BSD 3-Clause 'Modified' License",
    keywords="pygnssutils pyubx2 pynmmeagps pyrtcm GNSS GPS GLONASS GALILEO BEIDOU UBX NMEA RTCM RTCM3 GIS u-blox",
    platforms="Windows, MacOS, Linux",
    project_urls={
        "Bug Tracker": "https://github.com/semuconsulting/pygnssutils",
        "Documentation": "https://github.com/semuconsulting/pygnssutils",
        "Sphinx API Documentation": "https://www.semuconsulting.com/pygnssutils",
        "Source Code": "https://github.com/semuconsulting/pygnssutils",
    },
    classifiers=[
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: BSD License",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    python_requires=">=3.7",
)
