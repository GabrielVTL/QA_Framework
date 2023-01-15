"""teste_bdd feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

valorConta = 0

@scenario('feature_teste.feature', 'Saque Bancario')
def test_saque_bancario():
    """Saque Bancario."""
    print("Fim do teste")
    pass


@given('que a conta esta com saldo positivo de 100')
def que_a_conta_esta_com_saldo_positivo_de_100():
    """que a conta esta com saldo positivo de 100."""
    global valorConta
    valorConta =100


@when('realizo o saque de 30')
def realizo_o_saque_de_30():
    """realizo o saque de 30."""
    global valorConta
    valorConta = valorConta - 30


@then('a conta deve permanecer com 70')
def a_conta_deve_permanecer_com_70():
    """a conta deve permanecer com 70."""
    global valorConta
    assert valorConta == 70

