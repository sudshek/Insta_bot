import requests
BASE_URL = "https://api.instagram.com/v1/users"
APP_ACCESS_TOKEN = "398715021.1c98adf.13e3472fd0914d20bcccb1bd9f89a038"
response = ""
user_id = 0

#function to get user id by entering user name
#def get_user_id(user_name):
user_name = raw_input("Enter the user you are looking for")
URL = BASE_URL + "/search?q=%saccess_token=%s" %(user_name,APP_ACCESS_TOKEN)
response = requests.get(URL)
print response.json()


import requests

r = requests.get('https://api.instagram.com/v1/users/2027554944/media/recent'
                 '?access_token=398715021.1c98adf.13e3472fd0914d20bcccb1bd9f89a038')
piyush_id = 2027554944
print r.json()
#media_id = r.json()["data"][0]['id']
user_id = r.json()['data'][0]['id']
print user_id
