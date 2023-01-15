Feature: teste_bdd

Scenario: Saque Bancario
    Given que a conta esta com saldo positivo de 100
    When realizo o saque de 30
    Then a conta deve permanecer com 70 