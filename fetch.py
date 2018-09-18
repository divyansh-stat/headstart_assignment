import click
import json 
import requests
import subprocess
import os

#@click.group()


@click.command()
def cli():
	"""This scripts greets you"""
	with open("token.txt") as file:
		token = file.read()

	token_py = json.loads(token)
	github_token = token_py['token']
	print github_token

	os.system('~/Documents/GitHub/headstart_assignment/fetch_issues.sh')

	with open("fetched_issues.txt") as file:
		issues = file.read()

	issues_processed = issues.replace('\r', ' ').replace('\n', ' ').replace(' \\ ','').replace('\\\\','').replace("u'",'')
	issues_list = json.loads(issues_processed)

	open("cleaned_issues_list.json", "w").write(json.dumps(issues_list, sort_keys=True, indent=4, separators=(',', ': ')))

	with open("cleaned_issues_list.json") as file:
		issues = file.read()
	issues_first = json.loads(issues)
	print json.dumps(issues_first[1:5], indent=4, sort_keys=True)
	
