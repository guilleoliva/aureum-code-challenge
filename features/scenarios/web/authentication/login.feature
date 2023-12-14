@SWAGS @AUREUM
Feature: Log in into Swags Lab's Web Page

  @SR-001 @SMOKE @REGRESSION
  Scenario: Log in with correct credentials
    Given Tom goes to "Swags Lab" Web APP login page
    Then Tom should see the "Swags Lab" icon present
    And Tom inputs his credentials as "STANDARD-USER"
    And Tom clicks on the Log in button
    Then Tom sees the dashboard

  @SR-002 @SMOKE @REGRESSION
  Scenario: Log in with incorrect credentials
    Given Tom goes to "Swags Lab" Web APP login page
    Then Tom should see the "Swags Lab" icon present
    And Tom inputs an incorrect password as "STANDARD-USER"
    And Tom clicks on the Log in button
    Then Tom sees the incorrect user/password message

  @SR-001F @FORCE-TO-FAIL
  Scenario: Log in with incorrect credentials - FORCE TO FAIL
    Given Tom goes to "Swags Lab" Web APP login page
    Then Tom should see the "Swags Lab" icon present
    And Tom inputs an incorrect password as "STANDARD-USER"
    And Tom clicks on the Log in button
    Then Tom sees the dashboard