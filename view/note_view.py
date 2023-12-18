class NoteView:
    def show_notes(self, notes):
        if notes:
            for note in notes:
                print(
                    f"ID: {note.id} заголовок: {note.title} текст: {note.message} дата/время: {note.timestamp}"
                )
        else:
            print("Заметок не найдено.")
        print()

    def show_note(self, note):
        if note:
            print(
                f"ID: {note.id} заголовок: {note.title} текст: {note.message} дата/время: {note.timestamp}"
            )
        else:
            print("Заметка не найдена.")
        print()

