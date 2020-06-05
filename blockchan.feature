Feature: Basic Blockchain tests

  Scenario: Create new wallet
    Given I am connected to Blockchain Wallet API
    When I create new wallets
    Then New wallets are created

  Scenario: Enable HD for wallet
    Given I am connected to Blockchain Wallet API
    When I enable HD for wallets
    Then Wallets have enabled HD

  Scenario: Check the balance of the wallet
    Given I am connected to Blockchain Wallet API
    When I check balance of account
    Then Account balance is returned
    And Account balance is printed

# TODO: this scenario does not work as intended, because balance is 0
  Scenario: Perform outgoing payment
    Given I am connected to Blockchain Wallet API
    When I perform outgoing payment
    Then Amount of bitcoins is transferred between accounts
