import click
import requests
from googletrans import Translator
from bs4 import BeautifulSoup


@click.group()
def cli():
    pass


@cli.command('conj')
@click.argument('verb')
@click.argument('n', required=False, default=-1)
def conjugate(verb, n):
    r = requests.get('https://www.spanishdict.com/conjugate/' + verb)
    soup = BeautifulSoup(r.text, 'html.parser')
    target = soup.find(class_='card')
    headers = target.find_all('span', class_='vtable-label-link-text')
    tables = target.find_all('table', class_='vtable')
    s = 0
    for i in range(len(headers)):
        if n != -1 and s == n:
            break
        header = headers[i].text
        table = tables[i]
        click.echo(click.style(header, fg='black', bg='white'))
        pretty_table(table)
        s += 1


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


@cli.command('tran')
@click.argument('text', nargs=-1)
def tran(text):
    text = ' '.join(text)
    translation = translate(text)
    click.echo(click.style(translation, fg='yellow'))

def translate(text):
    translator = Translator()
    if(translator.detect(text).lang == "en"):
        translated = translator.translate(text, dest="es")
    else:
        translated = translator.translate(text, dest="en")
    return translated.text

@cli.command('quiz')
@click.argument('vocab')
def quiz(vocab):
    click.echo()
    l = vocab.split(',')
    n = 1
    for word in l:
        word = word.strip()
        click.echo(str(n) + ') ' + word)
        guess = click.prompt('your answer').lower()
        answer = translate(word).lower()
        if correct(guess, answer):
            click.echo(click.style('correct!', fg='green'))
        else:
            click.echo(click.style('incorrect!', fg='red'))
        click.echo(click.style('the correct answer was: ' + answer, fg='yellow'))
        click.echo()
        n += 1

def correct(guess, answer):
    return guess == answer or guess in answer or answer in guess
