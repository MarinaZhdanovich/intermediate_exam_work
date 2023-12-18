import json

from model.note_model import NoteModel


class NoteStorage:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_notes(self, notes):
        notes_data = []
        for note in notes:
            notes_data.append(note.to_dictionary())
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(notes_data, file, indent=4, ensure_ascii=False)

    def load_notes(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                notes_data = json.load(file)
                notes = []
                for note in notes_data:
                    note_obj = self.create_note_from_dict(note)
                    notes.append(note_obj)
        except FileNotFoundError:
            notes = []
        return notes

    def create_note_from_dict(self, note_dict):
        note = NoteModel(title=note_dict['title'], message=note_dict['message'])
        note.id = note_dict['id']
        note.timestamp = note_dict['timestamp']
        return note
