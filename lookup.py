# Tested on 12-03-2020 1:42PM
# Contact: facebook.com/cse.tufayel
# Changes on twitter website will break down code and developer takes no responsibilities hereby
# Runs in 3 modes.
# 1. Direct code edit mode
# 2. Console mode (python lookup.py -u username)
# 3. Mass check mode (python lookup.py -l list.txt)
import requests
import json
import sys

username = "name" # change username here or run as python lookup.py -u username

def look(username):
    print("You are looking for '" + username + "'")
    url = "https://api.twitter.com/graphql/P8ph10GzBbdMqWZxulqCfA/UserByScreenName?variables=%7B%22screen_name%22%3A%22" + username + "%22%2C%22withHighlightedLabel%22%3Atrue%7D"
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,bn;q=0.8",
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        "content-type": "application/json",
        "dnt": "1",
        'origin': 'https://twitter.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36',
        'x-twitter-active-user': 'yes',
        'x-twitter-client-language': 'en'
        }
    resp  = json.loads(requests.get(url, headers=headers).text)
    # you can play around with resp variable output and get other profile info
    # such as follower, bio, display name, account creation time etc.
    try:
        print("Username unavailable since " + resp["data"]["user"]["legacy"]["created_at"])
    except:
        try:
            err = resp["errors"][0]["message"]
            if "Not found" == err:
                print("Username is available")
            else:
                print(err)
        except:
            print("Username is available")
        # this block of code(finally) can be removed if you dont need server response
        finally:
            print("*"*17)
            print("For debug output:")
            print("*"*17)
            print(resp)
            print("*"*30)

if len(sys.argv) > 2:
    if sys.argv[1] == "-l":
        try:
            user_list = open(sys.argv[2], "r").read().split("\n")
            for username in user_list:
                look(username)
        except:
            print("Recheck input file name again")
    else:
        look(sys.argv[2])
else:
    look(username)
