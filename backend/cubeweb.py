import random
from bottle import route, template, HTTPError, run
import database

card_db = database.get_card_database()
cube = database.get_cube()


@route("/")
def index():
    tmpl = """
    <a href="/api/cube/CompanionCube">(api)</a>
    <ul>
    % for card in cards:
    <li><a href="/card/{{ card }}">{{card}}</a></li>
    % end
    </ul>
    """

    return template(tmpl, cards=cube)

@route("/card/<card>")
def show_card(card):
    if card not in cube:
        raise HTTPError(404)
    
    tmpl = """
    <a href="/api/card/{{card.name}}">(api)</a>
    <h1>{{card.name}}</h1>
    <p>{{card.text}}</p>
    """

    return template(tmpl, card=card_db[card])

@route("/api/card/<card>")
def card_json(card):
    return card_db[card].to_dict()

@route("/api/cube/<cube_id>")
def cube_list(cube_id):
    return {
        "cube": "CompanionCube",
        "cards": cube.cards
    }

@route("/api/random_pair")
def random_pair_test():
    c1, c2 = random.sample(cube.cards, 2)
    return {
        "pair": [c1, c2]
    }


run(port=8080)