import json
file = 'username.json'
def get_stored_username():

    try:
        with open(file) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    username = get_stored_username()
    if username:#if username exists
        print(f'Welcome back {username}!')
    else:
        username = input('Please enter your name: ')
        with open(file,'w') as fo:
            json.dump(username,fo)
        print(f'We will remember you {username} when You come back.')

greet_user()