Feature: CRUD operations for evaluation scenario

  Background:
    Given creating-evaluation-scenario has 
      | use-case | requirement |
      | my-use-case1 | my-requirement1 |
    * Exists use case named my-use-case1
    * Exists requirement named my-requirement1
    * Exists requirement named my-requirement2
    * Exists requirement named my-requirement3
    * Exists VV method named my-VV-method1
    * Exists VV method named my-VV-method2
    * Exist VV method named my-VV-method3

  Scenario: Create a new evaluation scenario
    Given I am logged in as administrator
    When I create a new evaluation scenario with
      | use-case | requirement | VV-method |
      | my-use-case1 | my-requirement1 | my-VV-method1 |
    Then I should see evaluation with
      | see-item |
      | my-use-case1 |
      | my-requirement1 |
      | my-VV-method1 |

  Scenario: Update existing evaluation scenario (Add requirements)
    Given I am logged in as administrator
    And I have created evaluation scenario creating-evaluation-scenario
    When I add evaluation scenario requirements
      | requirement |
      | my-requirement2 |
      | my-requirement3 |
    Then I should see evaluation creating-evaluation-scenario with
      | see-item |
      | my-use-case1 |
      | my-requirement1 |
      | my-requirement2 |
      | my-requirement3 |

  Scenario: Update existing evaluation (Add VV method)
    Given I am logged in as administrator
    And I have created evaluation scenario creating-evaluation-scenario
    When I add evaluation scenario VV methods
      | VV-method |
      | my-VV-method1 |
      | my-VV-method2 |
      | my-VV-method3 |
    Then I should see evaluation creating-evaluation-scenario with
      | see-item |
      | my-use-case1 |
      | my-requirement1 |
      | my-VV-method1 |
      | my-VV-method2 |
      | my-VV-method3 |

  Scenario: Delete existing evaluation
    Given I am logged in as administrator
    And I have created evaluation scenario creating-evaluation-scenario
    When I remove creating-evaluation-scenario
    Then There shouldn't be creating-evaluation-scenario


