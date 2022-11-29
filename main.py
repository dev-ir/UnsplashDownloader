import sys
import os
import requests

# first application download collection from unsplash
# set collection id by array
# example id : 4762340 , you can use multi id collections.

collection_id = ['4762340']


def connect_api():

    # please for receive client id and secret id , got unsplash.com website
    per_page = '30'

    client_id = 'Srh9jgLzWZ-BTl_7pQbdZ7onIyjy7e3Btno2OIT6ojgs'
    secret_id = 'TNptlnkxV9kg2KRg_R7p3aMxR1HRNjxGGt5_29clsDY'

    url_api = "https://api.unsplash.com/collections/4762340/photos/?client_id=" + client_id+"&client_secret="+secret_id+"&per_page="+str(per_page)
    response = requests.get(url_api)
    if response.status_code != 200:
        print('error :' + str(response.status_code))

    data = response.json()


def response_code(code):
    match code:
        case 200:
            return {
                'label': 'success',
                'code': code,
            }
        case 400:
            return {
                'label': 'The request was unacceptable, often due to missing a required parameter',
                'code': code,
            }
        case 401:
            return {
                'label': 'Invalid Access Token',
                'code': code,
            }
        case 403:
            return {
                'label': 'Missing permissions to perform request',
                'code': code,
            }
        case 404:
            return {
                'label': 'The requested resource doesn’t exist',
                'code': code,
            }
        case 500:
            return {
                'label': 'Something went wrong on our end',
                'code': code,
            }


connect_api()
