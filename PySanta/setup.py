from setuptools import setup, find_packages

with open("README.md",'r') as f:
	long_description = f.read()

setup(
	name='PySanta',
	version='0.0.1', # PEP440
	description='PySanta is Libraray of multiple utitlity tools developed by Santo K Thomas. Corrently development of this library is in Alpha stage',
	long_description=long_description,
	long_description_content_type="text/markdown",
	py_modules=['PySanta','wify'], 
	#package_dir ={'':'src'},
	packages = find_packages(include=('PySanta','PySanta.*')),
	url='https://github.com/santokalayil/PySanta',
	author='Santo K Thomas',
	author_email='santokalayil@gmail.com',
	classifiers=[
			'License :: OSI Approved :: MIT License',
			'Programming Language :: Python :: 3',
			'Programming Language :: Python :: 3.7',
			'Programming Language :: Python :: 3.8',
			'Operating System :: OS Independent'
	],
	install_requires=['python-nmap==0.6.1',
					'json',

	],
	)