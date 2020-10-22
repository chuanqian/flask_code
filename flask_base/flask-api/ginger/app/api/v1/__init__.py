from flask import Blueprint
from app.api.v1 import user, book, client, token


def create_blueprint_v1():
    # from app.api.v1.book import api as book
    # from app.api.v1.user import api as user
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1)
    book.api.register(bp_v1)
    client.api.register(bp_v1)
    token.api.register(bp_v1)
    return bp_v1
