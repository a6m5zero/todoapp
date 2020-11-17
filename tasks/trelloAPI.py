import requests
import json

class TrelloAPI():
    def __init__(self, api_key, hash_key):
        self.query = {'key': api_key, 'token': hash_key}
    
    def get_boards(self):
        url = 'https://api.trello.com/1/members/me/boards'
        response = requests.request("GET", url, params = self.query)
        json_response = response.json()
        boards = {}
        for board in json_response:
            boards[board['name']] = board['id']
        return boards
    
    def get_cards_on_board(self, board_id):
        url = f'https://api.trello.com/1/boards/{board_id}/cards'
        response = requests.request("GET", url, params = self.query)
        json_response = response.json()
        cards = {}
        for card in json_response:
            cards[card['id']] = card['name']
        return(cards)


if __name__ == "__main__":
    pass