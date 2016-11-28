from slackclient import SlackClient
with open('/Users/randy/Documents/creds/slackkey.txt') as f:
    key = f.read()

sc = SlackClient(key)

userlist = sc.api_call("users.list", as_user="true:")
userdict = {}
for user in userlist['members']:
        if user['is_bot'] == True: continue
        if user['deleted'] == True: continue
        userdict[user['id']] = {'real_name' : user['profile']['real_name'],
        'first_name': user['profile']['first_name'],
        'last_name': user['profile']['last_name'],
        'name': user['name']}


print(userdict)
