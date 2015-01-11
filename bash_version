#!/bin/bash
curl --globoff --get 'http://en.wikipedia.org/w/api.php' --data-urlencode format="json" --data-urlencode action="query" --data-urlencode titles=NOTDONE --data-urlencode prop="extracts" --data-urlencode rvprop="content" --data-urlencode continue="" --data-urlencode exsectionformat="plain" --data-urlencode redirects=""

# In the above curl query, the parameter "title" is passed. I mean to make this into a command line option so any page can be accessed
