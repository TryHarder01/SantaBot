"""
The conversation logic to get the information from users
"""
username = 'NAME_GOES_HERE'

introduction = "Hello {}, before we start let me check if we've done this before...".format(username)

new= """Ok let's do this. I'm going to ask you for three things you like and three
things you don't like. Once everyone has done that, I'll mix and match everyone in the
company. You'll get matched to somoene in another department, and someone who isn't matched to you."""

dept_string = """First thing I need from you is your department. I'll give you a list of departments and I
need you to respond in the exact format so I can match it."""

dept_options = ['Analytics'
                'Marketing',
                'PD',
                'Merchants',
                'Accounting',
                'CS',
                'Tech',
                'Purchasing',
                'Creative',
                'Inbound',
                'Outbound',
                'Dropship',
                'Leadership',
                'UX'].sort()

dept_choice = "User_submits"

dept_correct = "Ok, {}, got it. Let's get to the good stuff.".format(dept_choice)
dept_wrong = "Not on my list. Here's the departments you can choose from. Where should I put you?" #add all departments

likes_intro = """In three separate messages, send me three things you like. For instance, I like: \n
interpreted languages\n
pelicans\n
peeled potatoes.\n
What's the first?"""
like_1_response = "like1"

likes_2_ask = "Your second like?"
like_2_response = "like2"

likes_3_ask = "Your third like?"
like_3_response = "like3"

likes_intro = """In three seperate messages, send me three things you do *not* like. For instance, I do *not* like: \n
baths\n
playing board games\n
iambic pentameter.\n
What's one thing you don't like?"""
dislike_1_response = "dislike1"

likes_2_ask = "Your second dislike?"
dislike_2_response = "dislike2"

likes_3_ask = "Your third dislike?"
dislike_3_response = "dislike3"

review= """Whew. Ok. I think I have it, but check this over for me first.
You work in {dept_choice}. You like {like_1_response}, {like_2_response}, and {like_3_response}.
And you do *not* like {dislike_1_response},{dislike_2_response}, and {dislike_3_response}. Is that right (yes / no)."""

review_response = "yes"

while review_response.lower() != 'yes':
    if review_response.lower() == 'no':
        fix = "ok, which part do you want to edit..."
        ##allow ways to get into the choices

    else:
        unknown = "I don't understand. Please enter yes or no."


"""
use this to handle timeouts
http://stackoverflow.com/questions/492519/timeout-on-a-function-call
"""
