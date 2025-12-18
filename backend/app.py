from flask import Flask, jsonify, request
from flask_cors import CORS
import redis
import json

app = Flask(__name__)
CORS(app)  # Разрешаем запросы с фронтенда

# Подключение к Redis
redis_client = redis.Redis(
    host='redis',
    port=6379,
    decode_responses=True
)

NOTES_KEY = 'notes'

# ============ Helper Functions ============
def get_notes():
    notes_json = redis_client.get(NOTES_KEY)
    return json.loads(notes_json) if notes_json else []

def save_notes(notes):
    redis_client.set(NOTES_KEY, json.dumps(notes))

# ============ API Endpoints ============
@app.route('/api/health', methods=['GET'])
def health():
    try:
        redis_client.ping()
        return jsonify({
            "status": "healthy",
            "service": "notes-api",
            "redis": "connected"
        }), 200
    except:
        return jsonify({"status": "unhealthy"}), 500

@app.route('/api/notes', methods=['GET'])
def get_all_notes():
    notes = get_notes()
    return jsonify(notes)

@app.route('/api/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Text is required"}), 400
    
    notes = get_notes()
    new_note = {
        'id': len(notes) + 1,
        'text': data['text'],
        'completed': False
    }
    notes.append(new_note)
    save_notes(notes)
    
    return jsonify(new_note), 201

@app.route('/api/notes/<int:note_id>/toggle', methods=['PUT'])
def toggle_note(note_id):
    notes = get_notes()
    for note in notes:
        if note['id'] == note_id:
            note['completed'] = not note['completed']
            save_notes(notes)
            return jsonify(note)
    
    return jsonify({"error": "Note not found"}), 404

@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    notes = get_notes()
    new_notes = [note for note in notes if note['id'] != note_id]
    
    if len(new_notes) == len(notes):
        return jsonify({"error": "Note not found"}), 404
    
    save_notes(new_notes)
    return jsonify({"success": True})

@app.route('/api/stats', methods=['GET'])
def get_stats():
    redis_client.incr('api_requests')
    requests_count = redis_client.get('api_requests') or 0
    
    return jsonify({
        "total_requests": requests_count,
        "notes_count": len(get_notes())
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)