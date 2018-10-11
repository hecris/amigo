from setuptools import setup

setup (
	name="amigo",
	version="1.0",
	py_modules=["amigo.amigo"],
	install_requires=[
		"Click",
		"Requests",
		"BeautifulSoup4",
		],
	entry_points="""
		[console_scripts]
		amigo=amigo.amigo:cli
	""",
	)
