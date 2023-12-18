class NoteModel:
    def __init__(self, title, message):
        self.id = None
        self.title = title
        self.message = message
        self.timestamp = None

    def to_dictionary(self):
        return {
            'id': self.id,
            'title': self.title,
            'message': self.message,
            'timestamp': self.timestamp
        }

