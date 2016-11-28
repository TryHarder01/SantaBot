def name_to_id(sc):
    """
    takes the api and returns a dictionary of the users with their handle
    as the dictionary key.
    """
    userlist = sc.api_call("users.list", as_user="true:")
    userdict = {}
    for user in userlist['members']:
        if user['is_bot'] == True: continue
        if user['deleted'] == True: continue
        userdict[user['name']] = {'real_name' : user['profile']['real_name'],
        'first_name': user['profile']['first_name'],
        'last_name': user['profile']['last_name'],
        'id': user['id']}
    return userdict


def id_to_name(sc):
    """
    takes the api and returns a dictionary of the users with their id
    as the dictionary key.
    """
    userlist = sc.api_call("users.list", as_user="true:")
    userdict = {}
    for user in userlist['members']:
        if user['is_bot'] == True: continue
        if user['deleted'] == True: continue
        userdict[user['id']] = {'real_name' : user['profile']['real_name'],
        'first_name': user['profile']['first_name'],
        'last_name': user['profile']['last_name'],
        'name': user['name']}
    return userdict
