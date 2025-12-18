# from flask import Flask, render_template, request, redirect, jsonify
# from redis import Redis
# import json

# app = Flask(__name__)
# redis = Redis(host='redis', port=6379, decode_responses=True)

# # Ключ для хранения заметок в Redis
# NOTES_KEY = 'notes'

# def get_notes():
#     """Получить все заметки из Redis"""
#     notes_json = redis.get(NOTES_KEY)
#     if notes_json:
#         return json.loads(notes_json)
#     return []

# def save_notes(notes):
#     """Сохранить заметки в Redis"""
#     redis.set(NOTES_KEY, json.dumps(notes))

# @app.route('/')
# def index():
#     """Главная страница с заметками"""
#     notes = get_notes()
    
#     # Счетчик просмотров
#     redis.incr('hits')
#     counter = redis.get('hits')
    
#     return render_template('index.html', notes=notes, counter=counter)

# @app.route('/add', methods=['POST'])
# def add_note():
#     """Добавить новую заметку"""
#     note_text = request.form.get('note_text', '').strip()
#     if note_text:
#         notes = get_notes()
#         # Создаем новую заметку с уникальным ID
#         new_note = {
#             'id': len(notes) + 1,
#             'text': note_text,
#             'completed': False
#         }
#         notes.append(new_note)
#         save_notes(notes)
    
#     return redirect('/')

# @app.route('/toggle/<int:note_id>', methods=['POST'])
# def toggle_note(note_id):
#     """Переключить статус выполнения заметки"""
#     notes = get_notes()
#     for note in notes:
#         if note['id'] == note_id:
#             note['completed'] = not note['completed']
#             break
#     save_notes(notes)
#     return jsonify({'success': True})

# @app.route('/delete/<int:note_id>', methods=['POST'])
# def delete_note(note_id):
#     """Удалить заметку"""
#     notes = get_notes()
#     notes = [note for note in notes if note['id'] != note_id]
#     save_notes(notes)
#     return jsonify({'success': True})

# @app.route('/clear', methods=['POST'])
# def clear_notes():
#     """Очистить все заметки"""
#     save_notes([])
#     return redirect('/')

# @app.route('/api/notes', methods=['GET'])
# def get_notes_api():
#     """API для получения заметок"""
#     notes = get_notes()
#     return jsonify(notes)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)