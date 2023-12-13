@SWAGS
Feature: Happy Path - Buyer's Complete Purchase Process

  Background:
    Given Tom goes to "Swags Lab" Web APP login page
    Then Tom should see the "Swags Lab" icon present
    And Tom inputs his credentials as "STANDARD-USER"
    And Tom clicks on the Log in button
    Then Tom sees the dashboard

  @SR_006 @SMOKE @REGRESSION
  Scenario: Add items Checkout and Pay
    And Tom wants to add the following items to his cart
    | Item Name                |
    | Sauce Labs Onesie        |
    | Sauce Labs Fleece Jacket |
    | Sauce Labs Bike Light    |
    Then Tom sees the shopping cart icon shows the "3" items added
    When Tom clicks on the shopping cart icon
    Then Tom sees the items correctly added to the cart
    And Tom clicks on checkout
    Then Tom fills the checkout information with his information "Tom" "Sawyer" and postal code "4000"
    Then Tom clicks on continue
    And Tom sees the checkout overview
    Then Tom confirm the subtotal price is correct
    When Tom clicks on finish to complete the purchase
    Then Tom sees his purchase now is complete