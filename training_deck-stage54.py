# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: TrainingDeck
import pickle, os

DECK_DIR = os.path.join(os.path.dirname(__file__), "deck_data")
FAV_FILE = os.path.join(DECK_DIR, "favourites.pkl")

def get_favourites():
    if not os.path.exists(FAV_FILE):
        return {}
    with open(FAV_FILE, "rb") as f:
        try:
            return pickle.load(f)
        except Exception:
            return {}

def save_favourites(favs):
    os.makedirs(DECK_DIR, exist_ok=True)
    with open(FAV_FILE, "wb") as f:
        pickle.dump(favs, f)

def add_to_favourites(topic_id):
    favs = get_favourites()
    favs[topic_id] = True
    save_favourites(favs)

def remove_from_favourites(topic_id):
    favs = get_favourites()
    favs.pop(topic_id, None)
    save_favourites(favs)

def is_fav(topic_id):
    return get_favourites().get(topic_id, False)

def starred_decks():
    return [t for t in get_favourites() if get_favourites().get(t)]
