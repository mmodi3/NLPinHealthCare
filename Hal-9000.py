
########### Python 2.7 #############
import httplib, urllib, base64

headers = {
    # Request headers includes endpoint key
    # You can use the authoring key instead of the endpoint key.
    # The authoring key allows 1000 endpoint queries a month.
    'Ocp-Apim-Subscription-Key': 'e74ec3d437c84103b0cda324cef1473e',
}

params = urllib.urlencode({
    # Text to analyze
    'q': 'advil?',
    # Optional request parameters, set to default values
    'verbose': 'false',
})

# HTTP Request
try:
    # LUIS endpoint HOST for westus region
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')

    # LUIS endpoint path
    # includes public app ID
    conn.request("GET", "luis/v2.0/apps/a7985484-8966-4125-969a-e13be956d301?subscription-key=e74ec3d437c84103b0cda324cef1473e&timezoneOffset=-360&q=" + params)

    response = conn.getresponse()
    data = response.read()

    # print HTTP response to screen
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
