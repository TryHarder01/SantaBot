import time

class talker:
    people = {}
    dept_options = []
    answers = {}
    progress = {'U34V2A6QN':{'intro' : 0 , 'dept' : [0,0] , 'likes': 0 , 'dislikes' : 0,
                             'confirm': {'first': 0, 'likes': [0,0], 'dislikes':[0,0]}, 'success':0,'followups':0} }

    def __init__(self, sc, userdict, dept_options):
        self.people = userdict
        self.sc = sc
        self.dept_options = dept_options
        #print(self.dept_options)

    def intro(self, userid):
        self.answers[userid] = {}
        introduction = "Hello *{}*, before we start let me check if we've done this before...".format(self.people[userid]['name'])
        new = "Ok let's do this. I'm going to ask you for three things you like and three " + \
        "things you don't like. Once everyone has done that, I'll mix and match everyone in the " + \
        "company. You'll get matched to somoene in another department, and someone who isn't matched to you. ( _reply to continue_ )"

        print(self.sc.api_call("chat.postMessage", as_user="true:", channel=userid, text=introduction))
        time.sleep(1)
        print(self.sc.api_call("chat.postMessage", as_user="true:", channel=userid,  text=new))
        #print(introduction)
        #print(new)

    def check(self):
        print(self.people)

    def ask_dept(self, userid):
        dept_string = "First thing I need from you is your department. I'll give you a list of departments and I " + \
                      "need you to respond in the _exact_ format so I can match it:"
        for dept in self.dept_options:
            dept_string += '\n'+dept
        print(self.sc.api_call("chat.postMessage", as_user="true:", channel=userid,  text=dept_string))
        #print(dept_string)

        #print(self.dept_options)

    def process_dept_response(self, userid, text):
        if text in self.dept_options:
            response = "Ok, *{}*, got it. Let's get to the good stuff.".format(text)
            self.answers[userid]['dept'] = text
            result = 1
        else:
            response = "Not on my list. Here's the departments you can choose from. Where should I put you?" #add all departments
            result = 0

        print(self.sc.api_call("chat.postMessage", as_user="true:", channel=userid,  text=response))
        return result

    def ask_likes(self, userid):
        response = "In three separate messages, send me three things you like. For instance, I like: \ninterpreted languages\npelicans\npeeled potatoes.\n\nWhat's your first?"
        print(self.sc.api_call("chat.postMessage", as_user="true:", channel=userid, text=response))

    def get_likes(self, userid, text):
        self.answers[userid]['likes'] = self.answers[userid].get('likes', [])
        print(self.answers[userid]['likes'])
        print('in likes')


        self.answers[userid]['likes'].append(text)
        print('appended')

        if len(self.answers[userid]['likes']) == 3:
            response = 'Ok you like: {} {} and {}'.format(self.answers[userid]['likes'][0], self.answers[userid]['likes'][1], self.answers[userid]['likes'][1])
            print(self.sc.api_call("chat.postMessage", as_user="true:", channel=userid, text=response))
            return 1

        else:
            return 0


    def ask_dislikes(self, userid):
        response = "In three seperate messages, send me three things you do *not* like. For instance, I do *not* like: \nbaths\nplaying board games\niambic pentameter.\n\nWhat's one thing you don't like?"
        print(self.sc.api_call("chat.postMessage", as_user="true:", channel=userid,  text=response))

    def get_dislikes(self, userid, text):
        self.answers[userid]['dislikes'] = self.answers[userid].get('dislikes', [])
        print(self.answers[userid]['dislikes'])
        print('in dislikes')

        self.answers[userid]['dislikes'].append(text)
        print('appended')

        if len(self.answers[userid]['dislikes']) == 3:
            response = 'Ok you don\'t like: {} {} and {}'.format(self.answers[userid]['dislikes'][0], self.answers[userid]['dislikes'][1],
                                                 self.answers[userid]['dislikes'][1])
            print(self.sc.api_call("chat.postMessage", as_user="true:", channel=userid, text=response))
            return 1

        else:
            return 0

    def get_details(self, userid):
        print(self.answers[userid])

    def ask_confirmation(self,userid):
        response = 'Is this correct:\nDept: {} \nLike 1:{}\nLike 2: {}\nLike 3: {}\nDislike 1: {}\nDislike 2: {}\nDislike 3: {}\n\n  _yes or no_ ?'.format(self.answers[userid]['dept'],
                                    self.answers[userid]['likes'][0],
                                    self.answers[userid]['likes'][1],
                                    self.answers[userid]['likes'][2],
                                    self.answers[userid]['dislikes'][0],
                                    self.answers[userid]['dislikes'][1],
                                    self.answers[userid]['dislikes'][2])
        print(self.sc.api_call("chat.postMessage", as_user="true:", channel=userid, text=response))

    def get_confirmation(self, userid, text):
        if text.lower().strip() == 'yes':
            print('success')
            return 1
        else:

            print('Do you want to change your likes?')
            #edit_likes = input()


    def ask_confirm_likes(self, userid):
        response  = 'Do you want to change your *likes*?'
        print(self.sc.api_call("chat.postMessage", as_user="true:", channel=userid, text=response))
        return 1

    def get_confirm_likes(self, userid, text):
        if text.lower().strip() == 'no':
            return 1
        else:
            return 0

    def ask_confirm_dislikes(self, userid):
        response  = 'Do you want to change your *dislikes*?'
        print(self.sc.api_call("chat.postMessage", as_user="true:", channel=userid, text=response))
        return 1

    def get_confirm_dislikes(self, userid,  text):
        if text.lower().strip() == 'yes':
            return 1
        elif text.lower().strip() == 'no':
            return 0
        else:
            response = "I didn't understand. Please write _yes_ or _no_"
            print(self.sc.api_call("chat.postMessage", as_user="true:", channel=userid, text=response))
            return None

    def success(self, userid):
        response = "All done. You'll get a ping when I match everyone up for gifting."
        print(self.sc.api_call("chat.postMessage", as_user="true:", channel=userid, text=response))
        return 1


    def action(self, userid, text):
        print(self.progress)
        if self.progress[userid]['intro'] == 0:
            self.intro(userid)
            self.progress[userid]['intro'] =  1
            print('intro complete')
            return

        elif self.progress[userid]['dept'][0] == 0:
            self.ask_dept(userid)
            self.progress[userid]['dept'][0] = 1
            print('asked dept')
            return

        elif self.progress[userid]['dept'][1] == 0:
            self.progress[userid]['dept'][1] =self.process_dept_response(userid, text)
            print('confirmed dept')
            self.ask_likes(userid)
            return

        elif self.progress[userid]['likes'] == 0:
            response = self.get_likes(userid, text)
            self.progress[userid]['likes'] = response
            if response == 1 and self.progress[userid]['dislikes'] == 0:
                self.ask_dislikes(userid)
            elif response == 1 and self.progress[userid]['dislikes'] == 1:
                # sent back from confirmation question
                pass
            return


#dislikes and prompt confirmation readout

        elif self.progress[userid]['dislikes'] == 0:
            response = self.get_dislikes(userid, text)
            self.progress[userid]['dislikes'] = response
            if response == 1:
                self.ask_confirmation(userid)
            else:
                pass
            return

#get confirmation done if 'yes'
# thinking about if no

        elif self.progress[userid]['confirm']['first'] == 0:
            self.progress[userid]['confirm']['first'] = 1

            #first time through after asking confirmation
            result  = self.get_confirmation(userid, text)
            if result == 1:
                self.progress[userid]['success']= self.success(userid)
            else:
                self.progress[userid]['confirm']['likes'][0] = self.ask_confirm_likes(userid)

        elif self.progress[userid]['confirm']['first'] == 1 and self.progress[userid]['success'] == 0:
            #asked about likes, catching response
            result = self.get_confirm_likes(userid, text)
            #
            #second time through after asking confirmation
            if result == 1:
                #if 1 means they want to change likes
                self.ask_likes(userid)
                #catch up at likes

                self.progress[userid]['confirm']['likes'][1]= self.ask_confirm_dislikes(user)
            else:
                self.progress[userid]['confirm']['likes'][0] = 0


        elif self.progress[userid]['success'] == 5:
            result = self.get_confirmation(userid)
            # return 1 if yes, 0 if no
            self.progress[userid]['confirm'] = result
            if result == 0:
                self.progress[userid]['likes'] = self.ask_confirm_dislikes()
                # turns to 0 if user asks to reset likes
            #else...return

        elif self.progress[userid]['success'] == 1:
            self.progress[userid]['followups'] += 1
            if self.progress[userid]['followups'] % 5 == 0:
                self.success(userid)
            else:
                pass

