@cucumber-basket
Feature: Cucumber Basket
  Carrying Cucumbers

  @add
  Scenario Outline: Add cucumbers to a basket
    Given the basket has "<initial>" cucumbers
    When "<some>" cucumbers are added to the basket
    Then the basket contains "<total>" cucumbers

    Examples: Amounts
      | initial | some | total |
      | 2       | 4    | 6     |
      | 3       | 5    | 8     |
      | 0       | 5    | 5     |

  @remove
  Scenario: Remove cucumbers from a basket
    Given the basket has "8" cucumbers
    When "3" cucumbers are removed from the basket
    Then the basket contains "5" cucumbers