
class AtomicCardsDatabase:
    def __init__(self, data):
        self.db = {name: AtomicCard(data) for name, data in data['data'].items()}
        
        # normalize names
        self.front_name = {
            card.face_name.lower(): name for name, card in self.db.items()
        }


    def __getitem__(self, name):
        if name in self.db: return self.db[name]
        return self.db[self.front_name[name.lower()]]
    

class CardFace:
    def __init__(self, data) -> None:
        self.data = data
    
    def __getattr__(self, key):
        if key in self.data:
            return self.data[key]
        raise AttributeError(key)
    
    def to_dict(self):
        return self.data


class AtomicCard:
    def __init__(self, data):
        self.faces = [CardFace(d) for d in data]
        self.front = self.faces[0]
        self.multi_face = len(self.faces) > 1

    @property
    def face_name(self):
        return self.front.data.get('faceName', self.front.name)

    def __getitem__(self, face):
        return self.faces[face]

    def __getattr__(self, key):
        # if self.multi_face:
        return getattr(self.front, key)

    def to_dict(self):
        return {
            "name": self.face_name,
            "faces": [face.to_dict() for face in self.faces]
        }


class Deck:
    def __init__(self, card_list=None) -> None:
        self.cards = card_list if card_list else []

    @classmethod
    def load(cls, fh):
        return cls(fh.read().splitlines())

    def __iter__(self):
        yield from self.cards

    def __contains__(self, key):
        return key in self.cards
