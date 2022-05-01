Feature: Logging into system as different user

  This feature is testing if logging into the system is working properly.
  It means user, which is logged in, can see only what he should and nothing
  less or more.

  Scenario: Update an existing standard
    Given I am logged in as administrator
    And There already exists standard named "my-standard1"
    When I change name of standard "my-standard1" to "my-standard1-updated"
    Then I should see "Changes saved"
    And I should find standard "my-standard1-updated"
    But I shouldn't find standard "my-standard1"