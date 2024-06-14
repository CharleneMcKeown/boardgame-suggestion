from flask import Flask, render_template, request
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

import requests
import xml.etree.ElementTree as ET

def get_user_collection(username):
    base_uri = "https://boardgamegeek.com/xmlapi2/"
    game_base_url = "https://boardgamegeek.com/boardgame/"
    endpoint = f"collection?username={username}&stats=1&own=1"  # Request only owned games with stats
    try:
        response = requests.get(base_uri + endpoint)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        collection = []
        for item in root.findall('item'):
            status = item.find('status')
            if status is not None and status.get('own') == '1':  # Check if the game is owned
                game_id = item.attrib['objectid']
                # Fetch detailed stats for each game
                game_stats_response = requests.get(f"{base_uri}thing?id={game_id}&stats=1")
                game_stats_root = ET.fromstring(game_stats_response.content)
                best_at_player_count = None
                game_types = []
                for poll in game_stats_root.findall('.//poll[@name="suggested_numplayers"]'):
                    votes = {}
                    for results in poll.findall('results'):
                        numplayers = results.attrib['numplayers']
                        best_votes = int(results.find(".//result[@value='Best']").attrib['numvotes'])
                        votes[numplayers] = best_votes
                    best_at_player_count = max(votes, key=votes.get)  # Find the player count with the most "Best" votes
                # Extract game types (categories)
                for link in game_stats_root.findall(".//link[@type='boardgamecategory']"):
                    game_types.append(link.attrib['value'])
                game = {
                    'id': game_id,
                    'name': item.find('name').text,
                    'image': item.find('image').text if item.find('image') is not None else 'No image available',
                    'best_at_player_count': best_at_player_count,
                    'types': game_types,  # Add game types to the game dictionary
                }
                collection.append(game)
        return collection
    except requests.RequestException as e:
        print(f"Failed to fetch user collection: {e}")
        return []

# Example usage
# collection = get_user_collection("your_username_here")
# print(collection)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        collection = get_user_collection(username)
        return render_template('collection.html', collection=collection)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)