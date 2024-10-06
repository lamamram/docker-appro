"""
module chargé avant tout module de test
adjancent ou enfant
"""
import pytest
from bank.account import Account
from bank.client import Client

# 1. la valeur de retour d'une fonction
# décorée par fixture est injectable 
# dans toute fonction de test
# 2. fixture autouse disponible dans tous
# les tests du scope (~=module) sans injection
# 3. le scope est la portée de la fixture
# la fixture est réutilisable sans recharger
# dans : la sessin pytest | le package | module | classe | fonction courant
# @pytest.fixture(autouse=True, scope="module")
# 4. params exécute les tests décorés autant de fois que sa longueur
# en injectant toutà tour les valeur dans l'attribut param
# de l'objet de contexte request

account_set = [
    (Account(k, Client(k)), b) for k,b in {1: 500.00, 2: 300.00}.items()
]

# @pytest.fixture(scope="module", params=[1, 2])
@pytest.fixture
def client(request):
    # c = Client(request.param)
    c = Client(1)
    yield c
    # Cleanup: libère la mémoire
    print("\nfree memory !\n")
    del c

# 1. fixture dans une fixture
@pytest.fixture
def account_1(client):
    return Account(1, client)

@pytest.fixture
def show_mesgs():
    print("\nbefore")
    yield
    print("\nafter")


# paramétrisation de tous les tests depuis conftest
def pytest_generate_tests(metafunc):
    # recherche dans les signatures de fct de tests
    if "balance" in metafunc.fixturenames:
        metafunc.parametrize("account,balance", account_set)

# actions custom sur la collecte des tests
# def pytest_collection_modifyitems(config, items):
#     for item in items:
#         item.add_marker("something_related_to_balance")