Feature: Logging into system as different user

  This feature is testing if logging into the system is working properly.
  It means user, which is logged in, can see only what he should and nothing
  less or more.

  Background:
    Given A global administrator named "administrator"
    And A global reviewer named "itsreviewer" which is public
    And a method named "administrators method" which is public
    And a tool named "administrators tool" which is public
    And a use case named "administrators use case" which is public
    And a organization named "administrators organization" which is public
    And a standard named "administrators standard" which is public

  Scenario Outline: Try to edit a webpage when not logged in
    Given I am on the main page
    When I go to <post>
    Then I shouldn't see "Control panel"
    But I can see <post>

    Examples:
      | post |
      | "administrators method" |
      | "administrators tool" |
      | "administrators use case" |
      | "administrators organization" |
      | "administrators standard" |

  Scenario: Try to edit method when not logged in
    Given I am on the main page
    When I go to "administrators method"
    Then I shouldn't see "Control panel"
    But I can see "administrators method"

  Scenario: Log in to administrator account
    Given I am on the main page
    And I am not logged in
    When I try to log in as administrator
    Then I should see "Control panel"
    And "administrator" in "Control panel"
    And I shouldn't see Log in

  Scenario: Log in to reviewer account
    Given I am on the main page
    And I am not logged in
    When I try to log in as itsreviewer
    Then I should see "Control panel"
    And "itsreviewer" in "Control panel"
    And I shouldn't see Log in

  Scenario: Log in to not existing account
    Given I am on the main page
    And user1 is not registered
    And I am not logged in
    When I try to log in as user1
    Then I should see "Login failed."

  Scenario: administrator logged out
    Given I am logged in as administrator
    When I try to log out
    Then I should see "Log in"
    And I shouldn't see "Control panel"

  Scenario Outline: itsreviewer tries to edit a webpage
    Given I am logged in as itsreviewer
    When I try to edit <post>
    Then I shouldn't see edit options 

    Examples:
      | post |
      | "administrators method" |
      | "administrators tool" |
      | "administrators use case" |
      | "administrators organization" |
      | "administrators standard" |

  Scenario: itsreviewer tries to create a new method
    Given I am on the main page
    And I am not logged in
    When I try to log in as itsreviewer
    Then I shouldn't see "Add new..."
