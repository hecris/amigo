from Click import click
import requests
from googletrans import Translator
from bs4 import BeautifulSoup

@click.group()
def cli():
	pass

@cli.command()
@click.argument('verb')
def conjugate(verb):
	r = requests.get('https://www.spanishdict.com/conjugate/' + verb)
	soup = BeautifulSoup(r.text, 'html.parser')
	target = soup.find(class_='card')
	headers = target.find_all('span', class_='vtable-label-link-text')
	tables = target.find_all('table', class_='vtable')
	for i in range(len(headers)):
		header = headers[i].text
		table = tables[i]
		click.echo(click.style(header, fg='black', bg='white'))
		pretty_table(table)

def pretty_table(html):
	space = ' '
	# number of columns
	n = len(html.find('tr'))
	# get all td elements in table
	data = html.find_all('td')
	# this is the string to build upon. it represents one row
	build = "|"

	for i in range(len(data)):
		td = data[i].text
		# each cell in the table will be allowed 22 characters.
		# the remaining will be filled with spaces.
		# we use the vertical bar character to separate the cells
		diff = 22 - len(td)
		build = build + td + diff * space + '|'
		colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
		# if row is complete, echo it
		if (i + 1) % n == 0:
			click.echo(click.style(build, fg=colors[i // n]))
			build = "|"

@cli.command()
@click.argument('text', nargs=-1)	
def translate(text):
	#join tuple of args coming from command line
	text = ' '.join(text)

	#new Translator object
	translator = Translator()

	#detect language and trnaslate to either spanish or english
	if(translator.detect(text).lang == "en"):
		translated = translator.translate(text, dest="es")
	else:
		translated = translator.translate(text, dest="en")

	click.echo(translated.text)
