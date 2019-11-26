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
def servers(server):
  response = send_request("servers",server)
  result = []
  for server in response['data']:
    result.append(server['id'])
  print(json.dumps(result))
  pass

@main.command()
@click.pass_obj
def listeners(server):
  response = send_request("services",server)
  result = []
  for servers in response['data']:
    for listener in servers['attributes']['listeners']:
      if listener['attributes']['parameters']['port'] is not None:
        result.append(
          {
            "id":listener['id'],
            "port": listener['attributes']['parameters']['port']
          })
  print(json.dumps(result))
  pass

@main.command()
@click.pass_obj
def connections(server):
  response = send_request("connections",server)
  result = []
  pass

@main.command()
@click.pass_obj
def monitors(server):
  response = send_request("monitors",server)
  result = []
  for server in response['data']:
    result.append({
      "id": server['id']
    })
  print(json.dumps(result))
  pass

@main.command()
@click.pass_obj
def services(server):
  response = send_request("services",server)
  result = []
  for server in response['data']:
    result.append(server['id'])
  print(json.dumps(result))
  pass

if __name__ == "__main__":
  main()


