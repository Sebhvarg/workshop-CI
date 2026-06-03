import json
import os
DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")
def load_data():
    
    if not os.path.exists(DB_FILE):
        default_data = {
            "books": {
                "101": {"title": "El ingenioso hidalgo Don Quijote de la Mancha", "author": "Miguel de Cervantes"},
                "102": {"title": "Cien años de soledad", "author": "Gabriel García Márquez"},
                "103": {"title": "Ficciones", "author": "Jorge Luis Borges"},
                "104": {"title": "Pedro Páramo", "author": "Juan Rulfo"},
                "105": {"title": "La ciudad y los perros", "author": "Mario Vargas Llosa"}
            },
            "members": {},
            "loans": []
        }
        save_data(default_data)
        return default_data
    with open(DB_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {
                "books": {},
                "members": {},
                "loans": []
            }

def save_data(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
