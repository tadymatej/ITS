from behave import *
from valu3sUT import *

@when("I create a new organization without title")
def i_create_a_new_organization_without_title(context):
    web = context.valu3sWeb#type: Valu3sUT
    web.organizationsPage.open()
    
    web.loggedInMenu.addNewForm.add_organization()
    web.loggedInMenu.addNewForm.organizationForm.fill_in("", "summary", "acronym")
    web.loggedInMenu.addNewForm.organizationForm.submit()



@then('I shouldn\'t find organization "{name}"')
def i_shouldnt_find_organization(context, name):
    web = context.valu3sWeb#type: Valu3sUT
    web.organizationsPage.open()
    try:
        web.organizationsPage.find_organization_by_name(name)
        raise Exception("i shouldnt find organization")
    except(Exception):
        pass

@given('organization "{organization}" does not exists')
def organization_does_not_exist(context, organization):
    web = context.valu3sWeb#type: Valu3sUT
    
    web.organizationsPage.open()
    try:
        org = web.organizationsPage.find_organization_by_name(organization)
        web.organizationsPage.get_clickable_element_from_organization(org).click()
        web.loggedInMenu.actions()
        web.loggedInMenu.actionsForm.delete()
    except(Exception):
        pass

@when('I create a new organization named "{organization}" without ACRONYM')
def i_create_a_new_organization_named_without_acronym(context, organization):
    web = context.valu3sWeb#type: Valu3sUT
    web.organizationsPage.open()
    
    web.loggedInMenu.addNewForm.add_organization()
    web.loggedInMenu.addNewForm.organizationForm.fill_in(organization, "summary", "", "www.url.cz", "me", "me@gmail.com", "description")
    web.loggedInMenu.addNewForm.organizationForm.submit()

@when('I create a new organization named "{organization}" with ACRONYM "{acronym}"')
def i_create_a_new_organization_named_with_acronym(context, organization, acronym):
    web = context.valu3sWeb#type: Valu3sUT
    web.organizationsPage.open()
    
    web.loggedInMenu.addNewForm.add_organization()
    web.loggedInMenu.addNewForm.organizationForm.fill_in(organization, "summary", acronym, "www.url.cz", "me", "me@gmail.com", "description")
    web.loggedInMenu.addNewForm.organizationForm.submit()

