from setuptools import find_packages
from numpy.distutils.core import Extension, setup

setup(
    name='radbelt',
    description='Astropy-friendly wrapper for the AE-8/AP-8 Van Allen belt model',
    author='Leo Singer',
    author_email='leo.p.singer@nasa.gov',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Astronomy"
    ],
    license='NOSA',
    python_requires='>=3.7',
    ext_modules=[
        Extension('radbelt.core',
            [
                'radbelt/core.pyf',
                'radbelt/core.f',
                'radbelt/extern/ccmc/igrf/shellig.f',
                'radbelt/extern/ccmc/aep8/trmfun.f'
            ]
        )
    ],
    install_requires=['astropy', 'numpy'],
    packages=find_packages(),
    package_data={
        'radbelt.extern.ccmc.igrf': ['*.dat'],
        'radbelt.extern.ccmc.aep8': ['*.asc']
    },
    zip_safe=False
)
