# API Backend for Cube Tune

* `/api/card/<card name>` - get data on card
* `/api/cube/<cube id>` - get list of cards in a particular cube (right now any id points to the sample cube)
* `/api/random_pair` - random pair of cards from the cube

## Requirements
Python packages:
* bottle

Also requires database download from mtgjson.com (place in db folder)
* [AtomicCards.json](https://mtgjson.com/api/v5/AtomicCards.json)

## Run
`python cubeweb.py`

Will listen on localhost:8080
