import json
import requests

#create an authorization url
protocol = "https"
location = "accounts.spotify.com"
auth_resource = "/authorize"
authurl_fmt = "{}://{}{}"
authurl = authurl_fmt.format(protocol, location, auth_resource)

#create a url query using information of main user from the json file
urlquery = {}
urlquery['client_id'] = '95da2990eb16408a96a93cfa3f27555c'
urlquery['redirect_uri'] = 'https://localhost/callback/'
urlquery['response_type'] = 'code'
urlquery['state'] = '1234567890'
urlquery['scope'] = "user-follow-read user-top-read user-read-recently-played user-library-read"
urlquery
session = requests.Session()
p = requests.Request('GET', authurl, params=urlquery).prepare()
print("Authorization url:",p.url)

url = 'https://accounts.spotify.com/api/token'
bodyparams = {'client_id':'95da2990eb16408a96a93cfa3f27555c','client_secret':'86caad313351402fb28adc216fe6a44d','grant_type': 'authorization_code', 'code': 'AQCMVFYoFddzFsy-eFo0CZxOYy5OyTM6SGHIKQzl1h-dgrT0LNGL5uHXLvnWZdJKBFfs6GYg6AhdHWXcKbvONytC0FOZD1r6k6XLPi9z0kECUVNKhXmsbBhKTqGduj4EBdjB8OxVkMSElGyxeKXIaKN30Ij4vtVcM7FAbqNgNpX_pYhqog9up3a_VDbK9iukzPmcSsarKnsUkK2JFtNxKvXEGGxn1M8yJkQFqfy41DuuQfrA3IWqhxk5Xexih5I18iBMfEVZPhJrjsgmzXs','redirect_uri':'https://localhost/callback/','scope': 'user-follow-read user-top-read user-read-recently-played user-library-read'}
resp = requests.post(url, data=bodyparams)
creds = resp.json()
print("Initial access token and refresh token:",resp.json())

item = 'AQD91c6vyO5gTlO1lYUBlu_COiWtOzNZ5nlCxyvEuxb5_O6g-phehcflEbp5t6IU5yhfcfLPMbXubi3Nv_bQrfRK2iKVJOhCXKy4jxgPvG_XyL5VSbtpV9E93C_Vvit1kiQ'
url1 = 'https://accounts.spotify.com/api/token'
bodyparams = {'client_id':'95da2990eb16408a96a93cfa3f27555c','client_secret':'86caad313351402fb28adc216fe6a44d','grant_type': 'refresh_token', 'refresh_token': '','redirect_uri':'https://localhost/callback/','scope': 'user-follow-read user-top-read user-read-recently-played user-library-read'}

bodyparams['refresh_token'] = item

resp2 = requests.post(url1, data=bodyparams)
newAccess = resp2.json()['access_token']
print("New access token:",resp2.json())

url = 'https://api.spotify.com/v1/me/following?type=artist'
headerAccess = {"Authorization": "Bearer " + newAccess}
resp3 = requests.get(url, headers = headerAccess)
print (resp3.json())

url1 = 'https://api.spotify.com/v1/me/tracks'
headerAccess = {"Authorization": "Bearer " + newAccess}
resp4 = requests.get(url1, headers = headerAccess)
print (resp4.json())

url2 = 'https://api.spotify.com/v1/me/top/tracks'
headerAccess = {"Authorization": "Bearer " + newAccess}
resp5 = requests.get(url2, headers = headerAccess)
print (resp5.json())