from slackclient import SlackClient
from bot_tools import id_to_name, name_to_id
import time
from bot_chatter import talker

with open('/Users/randy/Documents/creds/slackkey.txt') as f:
    key = f.read()

sc = SlackClient(key)
id_dict = id_to_name(sc)
name_dict = name_to_id(sc)

dept_options = ['Analytics','Marketing','PD', 'Merchants','Accounting','CS','Tech','Purchasing','Creative','Inbound','Outbound','Dropship','Leadership','UX']
dept_options.sort()

santabot = talker(sc, id_dict, dept_options)


#botid U3501E2T1

READ_WEBSOCKET_DELAY = 1

BOT_ID = 'U3501E2T1'

if sc.rtm_connect():
    while True:
        firehose = sc.rtm_read()
        #print(firehose)
        if firehose:
            channel = firehose[0].get('channel')
            text = firehose[0].get('text')
            user = firehose[0].get('user')
            if channel and text and user and (user != BOT_ID):
                # making sure I'm not reacting to my own msgs
                print(channel, text, user )
                if channel.startswith('D'):
                    # "D" for direct message
                    santabot.action(user, text)
        time.sleep(1)
else:
    print("Connection Failed, invalid token?")

"""
# didn't confirm, needs to be asked about likes
                # result will be 1 if asked to change likes, 0 if no

"""
"""
if self.progress[userid]['likes'] == 0:


elif self.progress[userid]['success'] == 15:
   #if 1 means they want to change likes
   print('here, now what')
   # now next 3 times i need to process them
   self.progress[userid]['confirm']['likes'][1]= self.ask_confirm_dislikes(userid)
else:
   print('here in else')
   #self.progress[userid]['confirm']['likes'][0] = 0
   """
