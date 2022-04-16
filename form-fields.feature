Feature: Testing required and not required form fields

    Scenario: Create organization when required field is not filled in
      Given I am logged in as administrator
      When I create a new organization without title
      Then I should see "Error"
      And I shouldn't find organization named ""

    Scenario: Create organization when required field is filled in
      Given I am logged in as administrator
      And organization "organization1" does not exist
      When I create a new organization named "organization1" without ACRONYM
      Then I should see "Error"
      And I shouldn't find organization named "organization1"

    Scenario: Create valid organization
      Given I am logged in as administrator
      And organization "organization1" does not exists
      When I create a new organization named "organization1" with ACRONYM "ACRO"
      Then I should find organization named "organization1"