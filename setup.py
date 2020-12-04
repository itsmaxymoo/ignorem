from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name='ignorem',
	version='0.1',
	packages=['ignorem'],
	url='https://github.com/itsmaxymoo/ignorem',
	license='Mozilla Public License version 2.0',
	author='Max Loiacono',
	author_email='',
	description='Easily manage .gitignore files.',
	long_description=long_description,
	long_description_content_type="text/markdown",
	entry_points={
		'console_scripts': ['ignorem=ignorem:main']
	},
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6'
)
