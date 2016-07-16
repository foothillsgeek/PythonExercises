#!/usr/bin/python3

csvFile = open('csvdata.csv','r')
htmlFile = open('htmldata.html','w')

html_header = """
<html>
  <head>
    <title>CSV2HTML</title>
  </head>

  <body>
    <table>
"""

html_footer = """
    </table>
  </body>
"""

htmlFile.write(html_header)

for csvLine in csvFile:
  htmlLine = []
  csvCell = csvLine.split(',')
  for cellData in csvCell:
    htmlLine.append("<td>{}</td>".format(cellData.strip()))
  htmlRow = ''.join(htmlLine)
  htmlFile.write("      <tr>{}</tr>\n".format(htmlRow))

htmlFile.write(html_footer)

csvFile.close()
htmlFile.close()

