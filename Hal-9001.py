########### Python 3.6 #############
import requests
import sys

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'e74ec3d437c84103b0cda324cef1473e',
}

params ={
    # Query parameter
    'q': str(sys.argv[1]),
    # Optional request parameters, set to default values
    'timezoneOffset': '0',
    'verbose': 'false',
    'spellCheck': 'false',
    'staging': 'false',
}

try:
    r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/a7985484-8966-4125-969a-e13be956d301',headers=headers, params=params)
    print(r.json())

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################