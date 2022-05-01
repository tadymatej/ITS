from behave import *
from valu3sUT import *

@given('A global reviewer named "{reviewer}" which is public')
def a_global_reviewer_named_which_is_public(context, reviewer):
    pass

@given("user1 is not registered")
def user1_is_not_registered(context):
    pass

@given('I am not logged in')
def i_am_not_logged_in(context):
    web = context.valu3sWeb #type: Valu3sUT
    web.log_out()
    

@when('I try to log in as administrator')
def i_try_to_log_in_as_administrator(context):
    web = context.valu3sWeb #type: Valu3sUT
    web.log_in("administrator", "administrator")

@then("I shouldn't see Log in")
def i_shouldnt_see_log_in(context):
    web = context.valu3sWeb #type: Valu3sUT
    try:
        web.driver.find_element_by_xpath(web.logInButton)
        raise Exception("I shouldn't see Log in")
    except(Exception):
        pass

@when("I try to log in as itsreviewer")
def i_try_to_log_in_as_itsreviewer(context):
    web = context.valu3sWeb #type: Valu3sUT
    web.log_in("itsreviewer", "itsreviewer")

@when('I try to log in as user1')
def i_try_to_log_in_as_user1(context):
    web = context.valu3sWeb #type: Valu3sUT
    web.log_in("user1", "user1")

@when("I try to log out")
def i_try_to_log_out(context):
    web = context.valu3sWeb #type: Valu3sUT
    web.log_out()

@given("I am logged in as itsreviewer")
def i_am_logged_in_as_itsreviewer(context):
    web = context.valu3sWeb #type: Valu3sUT
    web.log_in("itsreviewer", "itsreviewer")

@when('I try to edit "{post}"')
def i_try_to_edit_post(context, post):
    pass

@then("I shouldn't see edit options")
def i_shouldnt_see_edit_options(context):
    web = context.valu3sWeb #type: Valu3sUT
    try:
        web.driver.find_element_by_xpath(web.loggedInMenu.editButton)
        raise Exception("I shouldn't see edit options")
    except(Exception):
        pass

@then('"{what}" in "{where}"')
def i_should_see_what_in_where(context, what, where):
    web = context.valu3sWeb #type: Valu3sUT
    if(where == "Control panel"):
        web.driver.find_element_by_xpath(web.loggedUserElement + "[contains(text(), '" + what + "')]")
