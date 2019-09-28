# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 16:17:00 2017

@author: Yoel Cortes-Pena
"""
from setuptools import setup
#from Cython.Build import cythonize
#import numpy

setup(
    name='biosteam',
    packages=['biosteam'],
    license='MIT',
    version='0.9.0',
    description='The Biorefinery Simulation and Techno-Economic Analysis Modules',
    long_description=open('README.rst').read(),
    #ext_modules=cythonize('biosteam/equilibrium/unifac.pyx'),
    #include_dirs=[numpy.get_include()],
    author='Yoel Cortes-Pena',
    install_requires=['pint==0.9', 'ht==0.1.52', 'fluids==0.1.74',
                      'scipy', 'IPython', 'thermo==0.1.39', 'colorpalette>=0.2.3',
                      'array_collections==0.1.9', 'free_properties==0.1.9',
                      'pandas', 'numpy', 'graphviz', 'matplotlib', 'lazypkg>=1.4',
                      'chaospy==3.0.11'],
    python_requires=">=3.6",
    package_data=
        {'biosteam': ['_equilibrium/*', 'inspect/*', 'price/*', '_report/*',
                      'utils/*', 'compounds/*',  'reaction/*',
				      'evaluation/*', 
					  'evaluation/evaluation_tools',
					  'units/*',
					  'units/designtools/*',
					  'units/facilities/*',
					  'units/decorators/*',
                      'biorefineries/*',
					  'biorefineries/lipidcane/*', 
                      'biorefineries/lipidcane/utils/*', 
                      'biorefineries/lipidcane/species/*',
                      'biorefineries/lipidcane/species/tripalmitin_liquid.xlsx', 
                      'biorefineries/lipidcane/system/*', 
                      'biorefineries/sugarcane/*',
                      'biorefineries/cornstover/*', 
                      'biorefineries/cornstover/_humbird2011.xlsx',
					  'my_units_defs.txt', 
                      ], },
    platforms=['Windows', 'Mac', 'Linux'],
    author_email='yoelcortes@gmail.com',
    url='https://github.com/yoelcortes/biosteam',
    download_url='https://github.com/yoelcortes/biosteam.git',
    classifiers=['Development Status :: 3 - Alpha',
                 'Environment :: Console',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Topic :: Scientific/Engineering',
                 'Topic :: Scientific/Engineering :: Chemistry',
                 'Topic :: Scientific/Engineering :: Mathematics'],
    keywords='chemical process simmulation bioprocess engineering mass energy balance material properties phase equilibrium CABBI biorefinery biofuel bioproducts',
)