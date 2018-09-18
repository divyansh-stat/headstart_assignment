import click


@click.group()
def cli():
	pass

@cli.command()
@click.option('--string', default="World", 
			help='This is the thing that is greeted')
@click.option('--repeat', default=1,
			help='How many times you should be greeted')
@click.argument('out', type=click.File('w'), default='-',required=False)	
def say(string,repeat,out):
	"""This scripts greets you"""
	click.echo(out)
	for x in xrange(repeat):
		click.echo('Hello %s!' % string,file=out)