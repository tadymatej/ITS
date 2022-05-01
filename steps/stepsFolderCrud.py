
from behave import *

@then('I can find "{folder}"')
def i_can_find_folder(context, folder):
    pass

@then('folder "{folder}" is empty')
def folder_is_empty(context, folder):
    pass

@given('folder named "{folder}" exists')
def folder_named_exists(context, folder):
    pass

@when('I try to rename folder named "{folder}" to "{folder_updated}"')
def i_try_to_rename_folder_named_to(context, folder, folder_updated):
    pass

@then('I can\'t find "{folder}"')
def i_cant_find_folder(context, folder):
    pass

@when('I try to delete folder named "{folder}"')
def i_try_to_delete_folder_named(context, folder):
    pass

@when('I try to create a new folder named "{name}" at home folder')
def i_try_to_create_a_new_folder_named_at_home_folder(context, name):
    pass

@when('I try to create a new folder with summary "{summary}"')
def i_try_to_create_a_new_folder_with_summary(context, summary):
    pass

@then('I should see a new folder with summary "{summary}"')
def i_should_see_a_new_folder_with_summary(context, summary):
    pass

@given('folder "{folder}" already exists at home folder')
def folder_already_exists_at_home_folder(context, folder):
    pass

@when('I try to create a new folder "{folder}" at home folder')
def i_try_to_create_a_new_folder_at_home_folder(context, folder):
    pass

@then('I shouldn\'t find "{folder}"')
def i_shouldnt_find_folder(context, folder):
    pass

@then('I shouldn\'t see more than one menu items named "{folder}"')
def i_shouldnt_see_more_than_one_menu_items_named(context, folder):
    pass