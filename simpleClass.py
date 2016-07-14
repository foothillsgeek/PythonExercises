#!/usr/bin/python3

import random

def genServerNames():
  serverAmount = 10
  serverNames = []
  for n in range(0, serverAmount, +1):
    serverNames.append("server"+str(n))
  return(serverNames)

def createServers(servers):
  server_instances = []
  for server in servers:
    print("Creating server with hostname " + str(server))
    server = Server(server)
    server_instances.append(server)
  return(server_instances)

class Server():
  def __init__(self, hostname):
    self.hostname = hostname
    self.memory = random.randrange(512,65536,512)
    self.disk = random.randrange(128,4096,128)
    print("Server with hostname " + self.hostname  + " created.")

serverNames = genServerNames()
servers = createServers(serverNames)

for server in servers:
  print("Hostname: " + server.hostname + '\t' + "Memory (MB): " + str(server.memory) + '\t' + "Disk Space: " + str(server.disk))
