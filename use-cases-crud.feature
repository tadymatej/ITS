Feature: CRUD operations for Use case

  Background:
    Given creating-use-case1 has 
      | my-organization1 |
      | my-evaluation-scenario1 |
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
      | my-evaluation-scenario2 |
      | my-evaluation-scenario3 |
    Then I should see use case creating-use-case1 with evaluation scenarios list with
      | my-evaluation-scenario1 |
      | my-evaluation-scenario2 | 
      | my-evaluation-scenario3 |

  Scenario: Add standards to use case
    Given I am logged in as administrator
    And I have created use case creating-use-case1 with case domain "Aerospace"
    When I add standards
      | my-standard1 | 
      | my-standard2 |
      | my-standard3 |
    Then I should see use case creating-use-case1 with standards
      | my-standard1 | 
      | my-standard2 |
      | my-standard3 |

  Scenario: Add partners to use case
    Given I am logged in as administrator
    And I have already created use case creating-use-case1 with case domain "Aerospace"
    When I add partners
      | my-organization2 |
      | my-organization3 |
    Then I should see use case creating-use-case1 with partners
      | my-organization2 |
      | my-organization3 |

  Scenario: Delete use case
    Given I am logged in as administrator
    And I have created use case creating-use-case1 with case domain "Aerospace"
    When I delete creating-use-case1
    Then There shouldn't be creating-use-case1


  #Scenario: Create a new use case with wrong ER binding (organization)
  #  Given I am logged in as administrator
  #  When I create a new use case "use-case1" with case domain "Aerospace" and evaluation scenario "my-evaluation-scenario1"
  #  Then I shouldn't find use case "use-case1" in Use Cases directory

  #Scenario: Create a new use case with wrong ER binding (domain)
  #  Given I am logged in as administrator
  #  When I create a new use case "use-case1" with provider "my-organization1" and evaluation scenario "my-evaluation-scenario1"
  #  Then I shouldn't find use case "use-case1" in Use Cases directory

  #Scenario: Create a new use case with wrong ER binding (evaluation scenario)
  #  Given I am logged in as administrator
  #  When I create a new use case "use-case1" with provider "my-organization" and case domain "Aerospace"
  #  Then I shouldn't find use case "use-case1" in Use Cases directory