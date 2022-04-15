Feature: Testing created content visibility
  
  This feature is testing, if private content is really private, and if public content is 
  really public.

  Background:
    Given A global administrator named "administrator"
    And a method named "administrators public method" which is public
    And a method named "administrators private method" which is private
    And a tool named "administrators public tool" which is public
    And a tool named "administrators private tool" which is private
    And a use case named "administrators public use case" which is public
    And a use case named "administrators private use case" which is private
    And a organization named "administrators public organization" which is public
    And a organization named "administrators private organization" which is private
    And a standard named "administrators public standard" which is public
    And a standard named "administrators private standard" which is private

  Scenario Outline: Unlogged user tries to see private content
    Given I am on the main page
    And I am not logged in
    When I try to find "<private_post>"
    Then I can't see "<private_post>" link

    Examples:
      | private_post |
      | administrators private method |
      | administrators private tool |
      | administrators private use case |
      | administrators private organization |
      | administrators private standard |

  Scenario Outline: Unlogged user tries to see public content
    Given I am on the main page
    And I am not logged in 
    When I go to "<public_post>"
    Then I can see "<public_post>"

    Examples:
      | public_post |
      | administrators public method |
      | administrators public tool |
      | administrators public use case |
      | administrators public organization |
      | administrators public standard |

  Scenario Outline: administrator tries to see his content
    Given I am on the main page
    And I am logged in as administrator
    When I go to "<post>"
    Then I ca see "<post>"

    Examples:
      | post |
      | administrators public method |
      | administrators public tool |
      | administrators public use case |
      | administrators public organization |
      | administrators public standard |
      | administrators private method |
      | administrators private tool |
      | administrators private use case |
      | administrators private organization |
      | administrators private standard |