import sys
import os
import requests
import sys;
import json

# user : http://pypi.python.org/pypi/termcolor
from termcolor import colored

# first application download collection from unsplash
# set collection id by array
# example id : 4762340 , you can use multi id collections.

def connect_api(collection_id):

    # please for receive client id and secret id , got unsplash.com website
    per_page = '30'

    client_id = 'Srh9jgLzWZ-BTl_7pQbdZ7onIyjy7e3Btno2OIT6ojg'
    secret_id = 'TNptlnkxV9kg2KRg_R7p3aMxR1HRNjxGGt5_29clsDY'
    collection_id = collection_id
    url_api = "https://api.unsplash.com/collections/"+collection_id+"/photos/?client_id=" + client_id+"&client_secret="+secret_id+"&per_page="+str(per_page)
    response = requests.get(url_api)
    if response.status_code != 200:
        print('error :' + str(response_code(response.status_code)['label']))

    data = response.json()
    print(data)


print( 'please enter you collection id from website : ' )
collection_id = input()

print( colored(collection_id , 'red',attrs=["reverse", "blink"]) )

if len(collection_id) != 0 :
    connect_api( collection_id )
