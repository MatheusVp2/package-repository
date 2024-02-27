from src.utils_rick_morty_sdk.rick_morty import RickMorty


service = RickMorty()

print(service.get_all_characters())