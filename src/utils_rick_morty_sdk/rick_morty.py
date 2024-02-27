import requests
from .models import Character, ResponseCharacter

class RickMorty:

    def __init__(self):
        self.url = "https://rickandmortyapi.com/api/character/"

    def get_character_by_id(self, id: int) -> Character:
        response = requests.get(self.url + str(id))
        return Character(**response.json())
    
    def get_all_characters(self) -> ResponseCharacter:
        response = requests.get(self.url)
        return ResponseCharacter(**response.json())