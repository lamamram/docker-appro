import sys, bottle, os, warnings
from base import base_path
from beaker.middleware import SessionMiddleware
from bank.client import Client
from bank.account import Account
from bank.user import UserProxy

warnings.filterwarnings(action='ignore')
base_path = os.path.abspath(os.path.dirname(__file__))
bottle.TEMPLATE_PATH.insert(0, f"{base_path}/views")
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}

def is_auth():
    s = bottle.request.environ.get('beaker.session')
    return "auth" in s and s["auth"]

app = SessionMiddleware(bottle.app(), session_opts)

@bottle.get("/static/css/<filename:re:.*\\.css>")
def send_css(filename):
    return bottle.static_file(filename, root=f'{base_path}/static/css')

@bottle.get("/static/vendor/<filename:re:.*\\.(css|js)>")
def send_vendor(filename):
    return bottle.static_file(filename, root=f'{base_path}/static/vendor')

defaults = {
    "client_id": 1,
    "modules" : ("profile", "account"),
    "title": "My Usine"
}

@bottle.route("/")
@bottle.view("login.tpl")
def login():
    if is_auth():
        bottle.redirect("/home")
    return defaults

@bottle.route("/", method='POST')
@bottle.view("login.tpl")
def do_login():
    username = bottle.request.forms.get('username')
    passwd = bottle.request.forms.get('passwd')
    user = UserProxy(username, passwd)
    if user.get_id():
        s = bottle.request.environ.get('beaker.session')
        s["auth"] = True
        s.save()
        bottle.redirect("/home")
    return defaults


@bottle.route("/home")
@bottle.view("index.tpl")
def index():
    if not is_auth():
        bottle.redirect("/")
    return defaults

@bottle.route("/profile/<client_id:int>")
@bottle.view("profile.tpl")
def profile(client_id):
    context = defaults.copy()
    context["client_id"] = client_id
    context["title"] = "My Profile"
    context["client"] =  Client(client_id)
    return context

@bottle.route("/account/<client_id:int>")
@bottle.view("account.tpl")
def account(client_id):
    context = defaults.copy()
    context["client_id"] = client_id
    context["title"] = "My account"
    context["account"] =  Account(client_id, Client(client_id))
    return context


@bottle.route("/logout")
def logout():
    s = bottle.request.environ.get('beaker.session')
    del s["auth"]
    s.save()
    bottle.redirect("/")

if __name__ == "__main__":
    bottle.run(app=app, host='poc-python-app', port=8080, debug=True, reloader=False)
