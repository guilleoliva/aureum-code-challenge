@SWAGS @AUREUM
Feature: Inventory Sorts

  Background:
    Given Tom goes to "Swags Lab" Web APP login page
    Then Tom should see the "Swags Lab" icon present
    And Tom inputs his credentials as "STANDARD-USER"
    And Tom clicks on the Log in button
    Then Tom sees the dashboard

  @SR-004 @REGRESSION
  Scenario Outline: Sort by Price "<order_type>"
    And Tom sees all the prices with no order
    And Tom clicks on sort items by price "<order_type>"
    Then Tom sees the items prices now are sorted correctly

    Examples:
    | order_type  |
    | high to low |

  @SR-005 @REGRESSION
  Scenario Outline: Sort by Name "<order_type>"
    And Tom sees all the names with no order
    And Tom clicks on sort items by name "<order_type>"
    Then Tom sees the items names now are sorted correctly

    Examples:
    | order_type  |
    | Z to A      |
