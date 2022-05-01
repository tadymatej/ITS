from behave import *

from valu3sUT import *

@when('I create a new standard named "{standard}"')
def i_create_a_new_standard_named(context, standard):
    web = context.valu3sWeb#type: Valu3sUT

    web.standardsPage.open()
    web.loggedInMenu.addNew()
    web.loggedInMenu.addNewForm.add_standard()
    sleep(1)
    web.loggedInMenu.addNewForm.standardForm.fill_in(standard, "summary")
    web.loggedInMenu.addNewForm.standardForm.submit()

@then('I should find standard "{standard}"')
def i_should_find_standard(context, standard):
    web = context.valu3sWeb#type: Valu3sUT
    web.standardsPage.open()
    web.standardsPage.find_standard_by_name(standard)

@given('There already exists standard named "{standard}"')
def there_already_exists_standard_named(context, standard):
    web = context.valu3sWeb#type: Valu3sUT
    web.standardsPage.open()
    web.log_in("administrator", "administrator")

    try:
        web.standardsPage.find_standard_by_name(standard)
    except(Exception):
        i_create_a_new_standard_named(context, standard)

@when('I change name of standard "{standard}" to "{standard_updated}"')
def i_change_name_of_standard_to(context, standard, standard_updated):
    web = context.valu3sWeb#type: Valu3sUT
    web.standardsPage.open()

    standard = web.standardsPage.find_standard_by_name(standard)
    standard = web.standardsPage.get_clickable_element_from_standard(standard)
    web.driver.execute_script("arguments[0].click()", standard)
    sleep(1)
    web.loggedInMenu.edit()
    sleep(1)
    web.loggedInMenu.addNewForm.standardForm.fill_in("_updated", "")
    web.loggedInMenu.addNewForm.standardForm.submit()


@then('I shouldn\'t find standard "{standard}"')
def i_shouldnt_find_standard(context, standard):
    web = context.valu3sWeb#type: Valu3sUT
    web.standardsPage.open()
    try:
        web.standardsPage.find_standard_by_name(standard)
        raise Exception("I shouldnt find standard {}".format(standard))
    except(Exception):
        pass

@when('I delete standard named "{standard}"')
def i_delete_standard_named(context, standard):
    web = context.valu3sWeb#type: Valu3sUT
    web.standardsPage.open()

    standard = web.standardsPage.find_standard_by_name(standard)
    standard = web.standardsPage.get_clickable_element_from_standard(standard)
    web.driver.execute_script("arguments[0].click()", standard)
    sleep(1)
    web.loggedInMenu.actions()
    web.loggedInMenu.actionsForm.delete()