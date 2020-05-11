""" from __future__ import print_function
import requests
import json
import cv2

addr = 'http://192.168.43.209:5000'
test_url = addr + '/api/test'

# prepare headers for http request  
content_type = 'image/jpeg'
headers = {'content-type': content_type}
a= 'hello Rane'
# send http request with image and receive response
response = requests.post(test_url, data=a, headers=headers)
# decode response
#print(json.loads(response.text)) """


import os
from time import sleep
hostname = "192.168.43.209" #example
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print(hostname, 'is up!')
else:
  print(hostname, 'is down!')

print("\n\nPinging continuously.....!!\n\n")
while(1):
    response = os.system("ping -c 1 " + hostname)
    sleep(1)
