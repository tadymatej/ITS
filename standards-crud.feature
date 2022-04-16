Feature: CRUD operations with standard

  Scenario: Create a new standard
    Given I am logged in as administrator
    When I create a new standard named "my-standard1"
    Then I should see "Item created"
    And I should find standard "my-standard1"

  Scenario: Update an existing standard
    Given I am logged in as administrator
    And There already exists standard named "my-standard1"
    When I change name of standard "my-standard1" to "my-standard1-updated"
    Then I should see "Changes saved"
    And I should find standard "my-standard1-updated"
    But I shouldn't find standard "my-standard1"

  Scenario: Delete an existing standard
    Given I am logged in as administrator
    And There already exists standard named "my-standard1"
    When I delete standard named "my-standard1"
    Then I shouldn't find standard "my-standard1"