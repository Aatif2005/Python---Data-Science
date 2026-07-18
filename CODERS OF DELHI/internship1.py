import json
def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)
        return data
data = load_data("data.json")
#print(data)

def display_user(data):
    print("Users and their connections\n")
    for user in data['users']:
        print(f"{user['name']} is friend with: {user['friends']} and liked pages are {user['liked_pages']}")
    print("Pages Information")
    for page in data['pages']:
        print(f"{page['id']}: {page['name']}")

display_user(data) 