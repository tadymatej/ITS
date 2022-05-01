Feature: CRUD operations with tools

  Background:
    Given creating-tool1 has
      | related-method |
      | related-method1 |
    * Exists method related-method1
    * Exists method related-method2
    * Exists method related-method3
    * Exists standard my-standard1
    * Exists standard my-standard2
    * Exists standard my-standard3
    * Exists test case my-test-case1
    * Exists test case my-test-case2
    * Exists test case my-test-case3

  Scenario: Create a new tool
    Given I am logged in as administrator
    When I create creating-tool1
    Then I should find tool creating-tool1 with
      | see-item |
      | related-method1 |

  Scenario: Add related methods to an existing tool
    Given I am logged in as administrator
    And There already exists tool creating-tool1
    When I add related methods to tool
      | related-method |
      | related-method2 |
      | related-method3 |
    Then I should find tool creating-tool1 with
      | see-item |
      | related-method1 |
      | related-method2 |
      | related-method3 |

  Scenario: Add standards to an existing tool
    Given I am logged in as administrator
    And There already exists tool creating-tool1    
    When I add standards to tool
      | standard |
      | my-standard1 |
      | my-standard2 |
      | my-standard3 |
    Then I should find tool creating-tool1 with
      | see-item |
      | related-method1 |
      | my-standard1 |
      | my-standard2 |
      | my-standard3 |

  Scenario: Add test case to tool:
    Given I am logged in as administrator
    And There already exists tool creating-tool1
    When I add test cases to tool
      | test-case |
      | my-test-case1 |
      | my-test-case2 |
      | my-test-case3 |
    Then I should find tool creating-tool1 with
      | see-item |
      | related-method1 |
      | my-test-case1 |
      | my-test-case2 |
      | my-test-case3 |

  Scenario: Delete an existing tool
    Given I am logged in as administrator
    And There already exists tool creating-tool1
    When I remove tool creating-tool1
    Then I shouldn't find tool creating-tool1