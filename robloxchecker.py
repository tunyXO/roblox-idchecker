# أنا سأعمل نائب الرئيس بجد جدا سأفجر

import requests

url = 'https://users.roblox.com/v1/users/'
id = '2460812989' # Input your desired ID here

userinfo = requests.get(url+id)
if userinfo.status_code == 200:
  data = userinfo.json()
  username = data['name']
  display_name = data['displayName']
  description = data['description']
  print(f"Username: {username}")
  print(f"Display name: {display_name}")
  print()
  print(f"description: {description}")
  print()
else:
  print('Error retrieving user info')

userhistory = requests.get(url+id+'/username-history')
if userinfo.status_code == 200:
  data = userhistory.json()
else:
  print("Error retrieving username history")
print('Past usernames:', end= ' ')
for i, username_data in enumerate(data["data"]):
    username = username_data["name"]
    print(username, end= '')
    if i < len(data["data"]) - 1:
        print(',', end= ' ')


        



