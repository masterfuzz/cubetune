import bottle
import database

card_db = database.get_card_database()
cube = database.get_cube()


@bottle.route("/")
def index():
    tmpl = """
    <ul>
    % for card in cards:
    <li><a href="/card/{{ card }}">{{card}}</a></li>
    % end
    </ul>
    """

    return bottle.template(tmpl, cards=cube)

@bottle.route("/card/<card>")
def show_card(card):
    if card not in cube:
        raise bottle.HTTPError(404)
    
    tmpl = """
    <h1>{{card.name}}</h1>
    <p>{{card.text}}</p>
    """

    return bottle.template(tmpl, card=card_db[card])

bottle.run()