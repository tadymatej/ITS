Feature: CRUD operations for evaluation scenario

  Background:
    Given Exists use case named my-use-case1
    * Exist requirement named my-requirement1
    * Exist requirement named my-requirement2
    * Exist requirement named my-requirement3

  Scenario: Create a new evaluation scenario
    Given I am logged in as administrator
    When I create a new evaluation scenario with
      | my-use-case1 | my-requirement1 |
    Then I should see evaluation with
      | my-use-case1 |
      | my-requirement1 |

  Scenario: Update existing evaluation scenario (Add requirements)
    Given I am logged in as administrator
    And I have created evaluation scenario with
      | my-use-case1 | my-requirement1 |
    When I add evaluation scenario requirements
      | my-requirement2 |
      | my-requirement3 |
    Then I should see evaluation with
      | my-use-case1 |
      | my-requirement1 |
      | my-requirement2 |
      | my-requirement3 |

