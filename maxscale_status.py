#!/usr/bin/python3
import requests
import click
import json
from requests.auth import HTTPBasicAuth

class Server(object):
    def __init__(self, host=None, port=8989, user='admin', password='mariadb'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        

def send_request(service, server):
  url = "http://{}:{}/v1/{}?pretty".format(server.host,server.port,service)
  result = requests.get(url, auth=HTTPBasicAuth(server.user, server.password))
  if result.status_code == 200:
    return result.json()
  else:
    print("Error: " + result)

@click.group()
@click.pass_context
@click.argument('host')
@click.option('--user', default='admin')
@click.option('--password', default='mariadb')
@click.option('--port', default='8989')
def main(ctx, host, user, password, port):
  ctx.obj = Server(host, port, user, password)
  
@main.command()
@click.pass_obj
@click.argument('dbserver')
@click.argument('key', default='connections')
def srvconns(server,dbserver,key):
  response = send_request("servers",server)
  result = []
  for server in response['data']:
    if server['id'] == dbserver:
      print(server['attributes']['statistics'][key])
  pass

@main.command()
@click.pass_obj
@click.argument('key')
def listeners(server,key):
  response = send_request("services",server)
  result = []
  for service in response['data']:
    for listener in service['attributes']['listeners']:
      if listener['id'] == key:
        print(listener['attributes']['state'])
  pass

@main.command()
@click.pass_obj
@click.argument('dbserver')
def servers(server,dbserver):
  response = send_request("servers",server)
  result = []
  for server in response['data']:
    if server['id'] == dbserver:
      print(server['attributes']['state'])
  pass

@main.command()
@click.pass_obj
@click.argument('key')
def monitors(server,key):
  response = send_request("monitors",server)
  result = []
  for monitors in response['data']:
    if monitors['id'] == key:
      print(monitors['attributes']['state'])
  pass

if __name__ == "__main__":
  main()


