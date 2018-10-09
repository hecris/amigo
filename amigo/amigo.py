import click
import requests
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
	n = len(html.find('tr'))
	data = html.find_all('td')
	build = "| "

	for i in range(len(data)):
		td = data[i].text
		diff = 20 - len(td)
		build = build + td + diff * space + '|'
		colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
		if (i + 1) % n == 0:
			click.echo(click.style(build, fg=colors[i // n]))
			build = "| "
		
