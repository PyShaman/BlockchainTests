Feature: Basic Blockchain tests

  Scenario: Create new wallet
    Given I am connected to Blockchain Wallet API
    When I create new wallet
    Then new wallet is created

  Scenario: Check the balance of the wallet
    Given I am connected to Blockchain Wallet API
    When I check balance of account
    Then Account balance is displayed

  Scenario: Perform outgoing payment
    Given I am connected to Blockchain Wallet API
    When I perform outgoing payment
    Then Amount of bitcoins is transferred between accounts

   Scenario: Send many transactions
     Given I am connected to Blockchain Wallet API
     When I send bitcoins for three recipients
     Then Three recipients receive their bitcoins
