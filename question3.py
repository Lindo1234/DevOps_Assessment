import os
import requests

website_url = ["http://www.stackoverflow.com"]
times = os.environ ['times']

OVERALL = 0 #overall time
for j in range(len(website_url)):
    if OVERALL < int(times) :
        s = requests.get(website_url[j])#requests
        total = s.elapsed #time
        print ('Website Url:' , website_url[j], "Total time: ", total , 'Times it hit the site:', times )
      

