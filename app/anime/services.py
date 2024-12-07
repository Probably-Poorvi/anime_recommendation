import requests

ANILIST_GRAPHQL_URL = "https://graphql.anilist.co"

def fetch_anime_by_name_or_genre(name: str = None, genre: str = None):
    query = """
    query ($name: String, $genre: String) {
      Media(search: $name, genre: $genre, type: ANIME) {
        id
        title {
          romaji
        }
        genres
        popularity
      }
    }
    """
    variables = {"name": name, "genre": genre}
    response = requests.post(ANILIST_GRAPHQL_URL, json={"query": query, "variables": variables})
    return response.json()
