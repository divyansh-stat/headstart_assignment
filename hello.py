import click
import json 
import requests
with open("token.txt") as file:
   token = file.read()

token_py = json.loads(token)
github_token = token_py['token']
print github_token


headers = {
    'Accept': 'application/vnd.github.squirrel-girl-preview',
}
params = (
    ('sort', '"comments"'),
)
response = requests.get('https://api.github.com/repos/vmg/redcarpet/issues/544', headers=headers, params=params, auth=(github_token, 'x-oauth-basic'))

#@click.group()
def cli():
	pass
#
#@cli.command()
#@click.option('--string', default="World", 
#			help='This is the thing that is greeted')
#@click.option('--repeat', default=1,
#			help='How many times you should be greeted')
#@click.argument('out', type=click.File('w'), default='-',required=False)	
#def say(string,repeat,out):
#	"""This scripts greets you"""
#	click.echo(out)
#	for x in xrange(repeat):
#		click.echo('Hello %s!' % string,file=out)