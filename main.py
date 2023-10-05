import requests
import time

# Put ur discord webhook here
webhook_url = 'UR WEBHOOK'

def get_uuid(username):
    url = 'https://api.mojang.com/users/profiles/minecraft/' + username
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['id']
    else:
        return None

def getCollection(user, key, profile, collection):
    # Send a request to the Hypixel API
    request_url = f"https://api.hypixel.net/skyblock/profiles?key={key}&uuid={get_uuid(user)}"
    api_response = requests.get(request_url)
    response_json = api_response.json()

    if api_response.json()["profiles"][0]["cute_name"] == profile:
        response_json = api_response.json()["profiles"][0]["members"][get_uuid(user)]["collection"][collection]
    elif api_response.json()["profiles"][1]["cute_name"] == profile:
        response_json = api_response.json()["profiles"][1]["members"][get_uuid(user)]["collection"][collection]
    elif api_response.json()["profiles"][2]["cute_name"] == profile:
        response_json = api_response.json()["profiles"][2]["members"][get_uuid(user)]["collection"][collection]
    elif api_response.json()["profiles"][3]["cute_name"] == profile:
        response_json = api_response.json()["profiles"][3]["members"][get_uuid(user)]["collection"][collection]
    else:
        return "couldnt find profile"
    
    return response_json

################# SETTINGS
key = "" # replace with ur api key run /api new in skyblock to get ur api key
username = "popiiumaa" # replace with your username
profile = "Pineapple" # replace with the profile you want to track
collection = "WHEAT" # replace with the collection you want
#################

startamount = getCollection(username, key, profile, collection)

while True:
    total = getCollection(username, key, profile, collection)
    session = total - startamount
    message = (
        f"Total {collection} collected for {username} on {profile}: {total}\n"
        f"Total {collection} this session for {username} on {profile}: {session}\n"
        "----------------------------------------------------------------------"
    )
    
    data = {'content': message}
    
    response = requests.post(webhook_url, json=data)
    
    if 200 <= response.status_code < 300:
        print("Stats sent to webhook successfully (:")
    else:
        print(f"Failed to send stats to weebhook :( Status Code: {response.status_code}")
    
    time.sleep(180)
