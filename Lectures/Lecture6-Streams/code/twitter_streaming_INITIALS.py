import twython
from twython import TwythonStreamer

OAUTH_TOKEN = "925147453711683584-uokSHRKQ9yE3O8oKWAK7Mx38Rc2uOoT"
OAUTH_TOKEN_SECRET = "6PgetgqMvotN1zdj4BvqeWFgYcGUJeV5tL2sn1CaH3IQq"
APP_KEY = "Ots6pNpRnsVYzZsjAR6RI6kud"
APP_SECRET = " HJ7ViQh3jB6odaYontvLrNVpBgU6m3k9TVmiZzVLOmhMZ7WQmv"

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        self.disconnect()

if __name__ == "__main__":
    stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.statuses.filter(track=['python', 'javascript', 'ruby'])