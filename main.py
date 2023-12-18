from controller.note_controller import NoteController
from model.note_storage import NoteStorage
from view.note_view import NoteView


def main():
    NOTES_FILE = "notes.json"
    storage = NoteStorage(NOTES_FILE)
    controller = NoteController(storage)
    view = NoteView()

    while True:
        print("Доступные команды:")
        print("add - Добавить заметку")
        print("list - Показать список заметок")
        print("show - Показать заметку")
        print("delete - Удалить заметку")
        print("edit - Редактировать заметку")
        print("exit - Выйти из программы")

        command = input("Введите команду: ")

        if command == "add":
            title = input("Введите заголовок заметки: ")
            message = input("Введите текст заметки: ")
            controller.create_note(title, message)
        elif command == "list":
            date_filter = input("Введите дату для фильтрации (YYYY-MM-DD): ")
            notes = controller.get_notes(date_filter)
            view.show_notes(notes)
        elif command == "show":
            note_id = int(input("Введите ID заметки для просмотра: "))
            note = controller.get_note_by_id(note_id)
            view.show_note(note)
        elif command == "delete":
            note_id = int(input("Введите ID заметки для удаления: "))
            controller.delete_note(note_id)
        elif command == "edit":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            message = input("Введите новый текст заметки: ")
            controller.edit_note(note_id, title, message)
        elif command == "exit":
            break
        else:
            print("Некорректная команда. Попробуйте снова.\n")


if __name__ == "__main__":
    main()