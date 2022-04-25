Feature: CRUD operations with organization
  
  Background:
    Given organization organization1 has data
      | Organization1 | my_summary | ACRONYM | https://google.com | me | me@email.com | description |

  Scenario: Create a new organization
    Given I am logged in as administrator
    When I create a new organization organization1
    Then I should see "Item created"
    And I shoud find organization1
    And I should see organization organization1 with data
      | Organization1 | my_summary | ACRONYM | https://google.com | me | me@email.com | description |

  Scenario: Update an existing organization
    Given I am logged in as administrator
    And organization organization1 is already created
    When I set to organization organization1 data
      | Organization1_updated | my_summary_updated | ACRONYM_updated | https://seznam.com | me_updated | me_updated@gmail.com | des_updated |
    Then I should see organization organization1 with data
      | Organization1_updated | my_summary_updated | ACRONYM_updated | https://seznam.com | me_updated | me_updated@gmail.com | des_updated |

  Scenario: Delete organization Organization1
    Given I am logged in as administrator
    And organization organization1 is already created
    When I delete organization organization1
    Then I shouldn't find organization1