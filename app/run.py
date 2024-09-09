from modules.pokemon import get_pokemon
import requests_cache
from flask import Flask, request

app = Flask(__name__)
requests_cache.install_cache()

@app.route('/', methods=['GET'])
def home():
    args = request.args

    dto = get_pokemon(args.get("pokemon"), args.get("xp"))
    return dto, 200


if __name__ == '__main__':
    app.run(port=8088)
