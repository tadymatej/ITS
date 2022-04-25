Feature: CRUD operations with folder

    Background:
      Given a global administrator named "administrator"

    Scenario: Craete a new folder
      Given I am logged in as administrator 
      When I try to create a new folder named "folder1" at home folder
      Then I should see "Item created"
      And I can find "folder1"
      But folder "folder" is empty
 
    Scenario: Rename folder
      Given I am logged in as administrator
      And folder named "folder1" exists
      When I try to rename folder named "folder1" to "folder1_updated"
      Then I should see "Changes saved"
      And I can find "folder1_updated"
      But I can't find "folder1"

    Scenario: Delete folder
      Given I am logged in as administrator
      And folder named "folder1" exists
      When I try to delete folder named "folder1"
      Then I shouldn't see "folder1"
      And I shouldn't find "folder1"

    Scenario: Create empty folder
      Given I am logged in as administrator
      When I try to create a new folder named "" at home folder
      Then I should see "Required input is missing"
      And I should see "Add folder"

    Scenario: Craete a new folder with summary description
      Given I am logged in as administrator
      When I try to create a new folder with summary "summary"
      Then I should see a new folder with summary "summary"

    #Is this bug or feature??
    Scenario: Create another same named folder at same directory
      Given I am logged in as administrator
      And folder "folder" already exists at home folder
      When I try to create a new folder "folder" at home folder
      Then I shouldn't see more than one menu items named "folder"