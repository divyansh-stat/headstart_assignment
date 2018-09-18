from setuptools import setup

setup(
	name='FetchIssues',
	version='1.0',
	py_modules=['fetch'],
	install_requires=[
	'Click',
	],
	entry_points='''
		[console_scripts]
		fetch=fetch:cli
		''',
)
