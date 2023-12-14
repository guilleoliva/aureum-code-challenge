@API @PET @SMOKE @SR-008
Feature: [API] Get pet by ID

  Background:
    Given A request to create a new pet through Petstore's API
    When the request is made to create a pet
    Then the user is told the request to create was successful

  Scenario: Get pet by ID
    When the user wants to get the recently created pet
    Then the user is told the get pet request was successful
    And the user verifies that all the pet information is correct
    And The pet is removed to keep the application clean
