from setuptools import setup
from os import path

# README file as long_description
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

setup(name='autorad',
		url='https://github.com/dhellfeld/autorad',
		license='TBD',
		author='dhellfeld',
		author_email='dhellfeld@lbl.gov',
		description='Framework for autonomous radiological source search algorithms',
		long_description=long_description,
		packages=['autorad'],
		include_package_data=True,
		platforms='any',
		classifiers=['Programming Language :: Python',
					'Development Status :: 4 - Beta',
					'Natural Language :: English',
					'Environment :: Web Environment',
					'Intended Audience :: Science/Research',
					'License :: TBD :: TBD',
					'Operating System :: OS Independent',
					'Topic :: Scientific/Engineering'])
