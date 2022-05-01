
from behave import *

from stepsCommon import *

#TODO data z table
@given('organization organization1 has data')
def organization_organization1_has_data(context):
    pass

@when("I create a new organization organization1")
def i_create_a_new_organization_organization1(context):
    pass

@then("I should find organization1")
def i_should_find_organization1(context):
    pass

@then('I should find organization named "{organization}"')
def i_should_find_organization_named(context, organization):
    pass

@then('I shouldn\'t find organization named "{organization}"')
def i_shouldnt_find_organization_named(context, organization):
    pass

#TODO data z table
@then("I should see organization organization1 with data")
def i_should_see_organization_organization1_with_data(context):
    pass

@given("organization organization1 is already created")
def organization_organization1_is_already_created(context):
    a_organization_named_which_is_public(context, "organization1")

#TODO: data z table
@when("I set to organization organization1 data")
def i_set_to_organization_organization1_data(context):
    pass

@when("I delete organization organization1")
def i_delete_organization_organization1(context):
    pass

@then("I shouldn't find organization1")
def i_shouldnt_find_organization1(context):
    pass