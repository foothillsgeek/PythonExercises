#!/usr/bin/python3

import argparse
import json
import urllib.request

# Set up argparser, add one argument option, parse it, and assign it to arguments
argparser = argparse.ArgumentParser()
argparser.add_argument("-u","--url", action="store", dest="url", help="URL to JSON data")
arguments = argparser.parse_args()

# User-Agent header is required by most sites
http_header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}

# Verify that there was a URL passed to the script
if not arguments.url:
  print("Please pass a JSON URL for parsing using the -u / --url flags.")
  exit()

# Try to set up the HTTP request. Catch exceptions with the URL formatting
try:
  http_request = urllib.request.Request(arguments.url, None, http_header)
except ValueError:
  print("There was an issue with the URL provided. Please check the URL and try again")
  exit()

# Try to initiate the HTTP request and report any errors received.
try:
  http_response = urllib.request.urlopen(http_request)
except urllib.error.HTTPError as error:
  print("An error code was recieved from the server: {}".format(error.code))
  exit()
except urllib.error.URLError as error:
  print("A URL error was received from the server: {}".format(error.args))
  exit()

# Read the request data
json_posts = http_response.read().decode('utf8')

# Pass the data to the JSON parser which returns a list of JSON objects
json_list = json.loads(json_posts)

# Loop through the list, then loop through the key:value pairs for each dict, printing them out
for element in json_list:
  for key in element.keys():
    print("{}: {}".format(str(key), str(element[key])))
  print("\n")
