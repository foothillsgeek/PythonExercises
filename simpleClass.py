#!/usr/bin/python3

import random

def genServerList():
  serverAmount = 10
  serverList = []
  for n in range(0, serverAmount, +1):
    serverList.append("server"+str(n))
  return(serverList)

def createServers(servers):
  for server in servers:
    print("Creating server with hostname " + str(server))
    server = Server(server)

class Server(hostname):
  hostname = None
  def __init__(self, hostname):
    self.hostname = hostname
    self.memory = random.randrange(512,65536,512)
    self.disk = random.randrange(128,4096,128)
    print("Server with hostname " + self.hostname  + " created.")


serverList = genServerList()
#print(serverList)
#createServers(serverList)

#for server in serverList:
#  server = Server(server)

#print(server0.hostname)

test = Server("testserver")

#for server in serverList:
#  print("Hostname: " + server.hostname + '\t' + "Memory (MB): " + server.memory + '\t' + "Disk Space: " + server.disk)
