Feature: CRUD operations for Use case

  Background:
    Given creating-use-case1 has 
      | organization | evaluation-scenario |
      | my-organization1 | my-evaluation-scenario1 |
    * Exists organization my-organization1
    * Exist organization my-organization2
    * Exist organization my-organization3
    * Exists evaluation scenario my-evaluation-scenario1
    * Exists evaluation scenario my-evaluation-scenario2
    * Exist evaluation scenario my-evaluation-scenario3
    * Exists standard my-standard1
    * Exists standard my-standard2
    * Exists standard my-standard3

  Scenario: Create a new use case
    Given I am logged in as administrator
    When I create use case creating-use-case1 with case domain "Aerospace"
    Then I should see "Item created"
    And I should see use case domain "Aerospace"
    And I should see evaluation scenarios list with "my-evaluation-scenario1"
    And I should see use case provider my-organization1

  Scenario: Change case domain to use case
    Given I am logged in as administrator
    And I have already created use case with case domain "Aerospace"
    When I change case domain to "Railway"
    Then I should see "Changes saved"
    And I should see case domain "Railway"

  Scenario: Add evaluation scenarios to use case
    Given I am logged in as administrator
    And I have created use case creating-use-case1 with case domain "Aerospace"
    When I add evaluation scenarios
      | evaluation-scenario |
      | my-evaluation-scenario2 |
      | my-evaluation-scenario3 |
    Then I should see use case creating-use-case1 with evaluation scenarios list with
      | see-item |
      | my-evaluation-scenario1 |
      | my-evaluation-scenario2 | 
      | my-evaluation-scenario3 |

  Scenario: Add standards to use case
    Given I am logged in as administrator
    And I have created use case creating-use-case1 with case domain "Aerospace"
    When I add standards
      | standard |
      | my-standard1 | 
      | my-standard2 |
      | my-standard3 |
    Then I should see use case creating-use-case1 with standards
      | see-item |
      | my-standard1 | 
      | my-standard2 |
      | my-standard3 |

  Scenario: Add partners to use case
    Given I am logged in as administrator
    And I have already created use case creating-use-case1 with case domain "Aerospace"
    When I add partners
      | organization |
      | my-organization2 |
      | my-organization3 |
    Then I should see use case creating-use-case1 with partners
      | see-item |
      | my-organization2 |
      | my-organization3 |

  Scenario: Delete use case
    Given I am logged in as administrator
    And I have created use case creating-use-case1 with case domain "Aerospace"
    When I delete creating-use-case1
    Then There shouldn't be creating-use-case1