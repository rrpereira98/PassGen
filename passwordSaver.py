import json


def savePasswd(filePath, data):
    with open ("data.json", "w") as f:
        json.dump(data, f)

def loadPasswds(filepath):
    with open("data.json", "r") as f:
        data = json.load(f)
        return data

# try:
#     data = loadPasswds("data.json")
# except:
#     data = {};
# key = "google"
# data[key] = "password"
# savePasswd("data.json", data)