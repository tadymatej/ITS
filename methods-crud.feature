Feature: CRUD operations with methods
  
  Background:
    Given creating-method-1 has 
      | related-method1 |
    * Exists method related-method1
    * Exists method related-method2
    * Exists method related-method3
    * Exists standard my-standard1
    * Exists standard my-standard2
    * Exists standard my-standard3
    * Exists tool my-tool1
    * Exists tool my-tool2
    * Exists tool my-tool3
    * Exists part method my-part-method1
    * Exists part method my-part-method2
    * Exists part method my-part-method3
    * Exists VV method named my-use-case1
    * Exists VV method named my-use-case2
    * Exist VV method named my-use-case3
    # context
    # workflow

    Scenario: Create a new evaluation method
      Given I am logged in as administrator
      When I try to create creating-method1
      Then I should see creating-method-1 with
        | related-method1 |

    Scenario: Add related methods to method creating-method-1
      Given I am logged in as administrator
      And There already exists creating-method-1
      When I add related methods to method
        | related-method2 |
        | related-method3 |
      Then I should find creating-method-1 with
        | related-method1 |
        | related-method2 |
        | related-method3 |
    
    Scenario: Add standards to method creating-method-1
      Given I am logged in as administrator
      And There already exists creating-method-1
      When I add standards to method
        | my-standard1 |
        | my-standard2 |
        | my-standard3 |
      Then I should find creating-method-1 with
        | related-method1 |
        | my-standard1 |
        | my-standard2 |
        | my-standard3 |

    Scenario: Add tools to method creating-method-1
      Given I am logged in as administrator
      And There already exists creating-method-1
      When I add tools to method
        | my-tool1 |
        | my-tool2 |
        | my-tool3 |
      Then I should find creating-method-1 with
        | related-method1 |
        | my-tool1 |
        | my-tool2 |
        | my-tool3 |

    Scenario: Add part-methods to method creating-method-1
      Given I am logged in as administrator
      And There already exists creating-method-1
      When I add part-methods to method
        | my-part-method1 |
        | my-part-method2 |
        | my-part-method3 |
      Then I should find creating-method-1 with
        | related-method1 |
        | my-part-method1 |
        | my-part-method2 |
        | my-part-method3 |

      Scenario: Add use cases to method creating-method-1
        Given I am logged in as administrator
        And There already exists creating-method-1
        When I add use cases to method
          | my-use-case1 |
          | my-use-case2 |
          | my-use-case3 |
        Then I should find creating-method-1 with
          | related-method1 |
          | my-use-case1 |
          | my-use-case2 |
          | my-use-case3 |

      Scenario: Remove existing method creating-method-1
        Given I am logged in as administrator
        And There already exists creating-method-1
        When I remove creating-method-1
        Then I shouldn't find creating-method-1