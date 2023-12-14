@SWAGS @AUREUM
Feature: Log out from Swags Lab's Web Page

  Background:
  Given Tom goes to "Swags Lab" Web APP login page
  Then Tom should see the "Swags Lab" icon present
  And Tom inputs his credentials as "STANDARD-USER"
  And Tom clicks on the Log in button
  Then Tom sees the dashboard

  @SR-003 @SMOKE @REGRESSION
  Scenario: Log out
    And Tom clicks on the burger menu
    When Tom clicks on Log out
    Then Tom logs out correctly