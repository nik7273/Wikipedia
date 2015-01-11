import json, requests, sys

title = sys.argv[1]
if " " in title:
    x = title.replace(" ", "_")
else:
    x = title

parameters = {'format' : 'json', 'action' : 'query', 'titles' : x, 'prop' : 'extracts', 'rvprop' : 'content', 'continue' : '', "exsectionformat" : "plain", "redirects" : ""}

r = requests.get('http://en.wikipedia.org/w/api.php', params=parameters)

data = r.json()

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

with open('data2.txt', 'w') as file2:
    file2.write(str(data["query"]["pages"]))

