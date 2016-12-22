# This class is use to store non-db models

class Message():
    messagetype = None
    title = None
    content = None

    def __init__(self, messagetype, title, content):
        self.messagetype = messagetype
        self.title = title
        self.content = content

    def __repr__(self):
        return "<Message messagetype:%r title:%r content:%r>" % (self.messagetype, self.title, self.content)

