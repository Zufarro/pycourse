import datetime
t = datetime.datetime.now()

class Messenger:
    name = "yam"
    @classmethod
    def send_message(cls,text):
        print(text)
        m = Message("",text,t)
        return m

class Message:
    def __init__(self,sender,text,time):
        self.sender = sender
        self.text = text
        self.time = time
