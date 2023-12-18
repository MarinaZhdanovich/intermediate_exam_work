from datetime import datetime

from model.note_model import NoteModel


class NoteController:
    def __init__(self, note_storage):
        self.note_storage = note_storage

    def create_note(self, title, message):
        note = NoteModel(title, message)
        notes = self.note_storage.load_notes()
        note.id = len(notes) + 1
        note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notes.append(note)
        self.note_storage.save_notes(notes)
        print('Заметка успешно сохранена\n')

    def get_notes(self, date_filter=None):
        notes = self.note_storage.load_notes()
        if date_filter:
            filtered_notes = []
            for note in notes:
                if note.timestamp.startswith(date_filter):
                    filtered_notes.append(note)
            return filtered_notes
        return notes

    def get_note_by_id(self, note_id):
        notes = self.note_storage.load_notes()
        for note in notes:
            if note.id == note_id:
                return note
        else:
            raise ValueError('Заметка с указанным ID не найдена')

    def edit_note(self, note_id, title, message):
        notes = self.note_storage.load_notes()
        for note in notes:
            if note.id == note_id:
                note.title = title
                note.message = message
                note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.note_storage.save_notes(notes)
                print('Заметка успешно отредактирована\n')
                break
        else:
            raise ValueError('Заметка с указанным ID не найдена')

    def delete_note(self, note_id):
        notes = self.note_storage.load_notes()
        for note in notes:
            if note.id == note_id:
                notes.remove(note)
                self.note_storage.save_notes(notes)
                print("Заметка успешно удалена\n")
                break
        else:
            raise ValueError('Заметка с указанным ID не найдена')