#!/usr/bin/python3

import json
import urllib.request

# User-Agent header is required by most sites
http_header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}

# Set up the HTTP request
http_request = urllib.request.Request("https://jsonplaceholder.typicode.com/posts", None, http_header)

# Initiate the request
http_response = urllib.request.urlopen(http_request)

# Read the request data
json_posts = http_response.read().decode('utf8')

# Pass the data to the JSON parser which returns a list of JSON objects
json_list = json.loads(json_posts)

# Loop through the list, then loop through the key:value pairs for each dict, printing them out
for element in json_list:
  for key in element.keys():
    print("{}: {}".format(str(key), str(element[key])))
  print("\n")
