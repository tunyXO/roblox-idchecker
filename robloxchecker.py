# Simple ROBLOX user info retriever via id.
# Written by tuny
import sys
import requests

thumbnail_url = 'https://thumbnails.roblox.com/v1/users/avatar?userIds='
url = 'https://users.roblox.com/v1/users/'
size = '420x420' # Sizes: 720x720, 420x420, 352x552...
format = 'Png' # Png or Jpeg
is_circular = 'false' # Determines if the thumbnail is Circular or not

while True:
    try:
        id = input('Enter ID: ') # Asks for ID
        userinfo = requests.get(url+id)
        if userinfo.status_code == 200:
          data = userinfo.json()
          username = data['name']
          display_name = data['displayName']
          description = data['description']
          print(f'Username: {username}')
          print(f'Display name: {display_name}')
          print(f'description: {description}')
        else:
          print('Error retrieving user info')

        userhistory = requests.get(url+id+'/username-history')
        if userhistory.status_code == 200:
          data = userhistory.json()
        else:
          print('Error retrieving username history')
        print('Past usernames:', end= ' ')
        for username_data in data['data']:
            username = username_data['name']
            print(username, end= ' ')

        userthumbnail = requests.get(thumbnail_url+id+'&size='+size+'&format='+format+'&isCircular='+is_circular)
        if userthumbnail.status_code == 200:
          data = userthumbnail.json()
          image = data['data'][0]['imageUrl']
          print('\n'+image)
        else:
          print('Error retrieving user thumbnail')

    except:
        print(f"An error occurred. Maybe the ID isn't valid. Try again.")

    while True:
        choice = input("Do you want to enter another ID? (y/n): ")
        if choice.lower() == "y":
            break
        elif choice.lower() == "n":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

  
  
  





