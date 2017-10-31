from tweepy import Stream, OAuthHandler, API, Cursor
from tweepy.streaming import StreamListener

cke = "3IKgJJ0FH3PJYk3pcN1x50GFd"
cse = "XFhMG4p9A0aFaorMiVULLVjjKHQO2LSin1qL0NlJiBUHa5UcIF"
ato = "915035385390157824-LKBwbfchhlRRs9oGQ1galob4wVwf3H4"
ase = "XkhiUESdgr1I63JASWmR7LdNu2kOS942Nj5l0F3qnP91k"

auth = OAuthHandler(cke, cse)
auth.set_access_token(ato, ase)

api = API(auth)

#for tuit in Cursor(api.home_timeline).items(5):
#     print(tuit.text)

#for seguidor in Cursor(api.friends).items():
#     print(seguidor._json)

#for tuit in Cursor(api.user_timeline).items(2):
#     print(tuit.text)

class TLListener(StreamListener):
    def on_data(self, raw_data):
        print(raw_data)
        return True

    def on_error(self, status_code):
        print(status_code)

twStream = Stream(auth, TLListener())
twStream.filter(track=["#prayforvegas"])