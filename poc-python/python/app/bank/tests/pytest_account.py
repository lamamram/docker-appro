import pytest
from bank.account import Account
from bank.client import Client
import warnings
import sys

# markers appliqués à toutes les fonctions de test
# pytestmark = [
#     pytest.mark.something_related_to_balance
# ]

# account_set = [
#     (Account(k, Client(k)), b) for k,b in {1: 500.00, 2: 300.00}.items()
# ]

accounts = [Account(k, Client(k)) for k in (1, 2)]
balances = (500.00, 300.00)

# markers
# 1. désactivation de warnings custom
#@pytest.mark.filterwarnings("ignore:.*collections")
# 2. ajout d'une fixture non injectée dans la fonction de test
# fourniture d'un calcul (Act)
# @pytest.mark.usefixtures("show_mesgs")
# 3. désacitver un test, avec ou sans raison
# @pytest.mark.skip
# @pytest.mark.skip(reason="BECAUSE")
# 4. skip sur une &valuation booléene
# @pytest.mark.skipif(sys.version_info < (3, 9), reason="BECAUSE")
# 5. expected fail
# @pytest.mark.xfail
# def test_balance(account_1):
# 6. injection d'une liste de valeurs dans certains champs de la signature
# @pytest.mark.parametrize("account,balance", account_set)
# @pytest.mark.parametrize("account", accounts)
# @pytest.mark.parametrize("balance", balances)
# 7. marker custom
# option -m <custom_maker> ou -m "not <custom1> and|or <custom2>"
# @pytest.mark.something_related_to_balance
def test_balance(account, balance):
    warnings.warn("blabla collections !")
    # Arrange (instance, connexion ...)
    # Act (calcul)
    # Assert
    # capture de sys.stdout => option -s
    # print(f"\nbalance: {account_1.getBalance()}\n")
    assert balance == account.getBalance()

def test_overdraft():
    account = Account(1, Client(1))
    account.withdraw(600)
    assert account.overdraft

@pytest.mark.parametrize("firstname,lastname", [("michel", "lefebvre")])
def test_client_name(account_1, firstname, lastname, monkeypatch):
    class MockClient:
        def get_full_name(self):
            return f"{firstname.capitalize()} {lastname.upper()}"
    monkeypatch.setattr(account_1, "_Account__client", MockClient())
    assert account_1.get_client_name() == "Michel LEFEBVRE"



