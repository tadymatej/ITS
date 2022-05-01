from lib2to3.pgen2 import driver
from tkinter import E
from behave import *

from valu3sUT import *

@given("I am logged in as administrator")
def i_am_logged_in_as_administrator(context):
    web = context.valu3sWeb #type: Valu3sUT
    web.homePage.open()
    res = web.log_in("administrator", "administrator")

    #web.loggedInMenu.addNewForm.add_use_case()
    #web.loggedInMenu.addNewForm.useCaseForm.fill_in("title", "summary", "1", "a", "Brno", ["organization1", "organization2"], "description", ["About"])

    
    #el = web.methodsPage.find_method_by_name("Source Code Static Analysis")
    #el = web.methodsPage.get_clickable_element_from_method(el)
    #web.driver.execute_script("arguments[0].click()", el)
    #sleep(1)
    #raise Exception(el.get_attribute("innerHTML"))

    #mp = SingleMethodPageUT(web.driver, "")
    #raise Exception(mp.get_title_content())

    #web.methodsPage.filter_by_first_character("s")
    #els = web.methodsPage.get_methods_list()
    #raise Exception(els[0].get_attribute("innerHTML"))

    #form = web.loggedInMenu.addNewForm.add_method()
    #form.open_relations_settings()
    #form.relatedMethodsInput.path_from_home()

@then('I should see "{string}"')
def i_should_see(context, string):
    web = context.valu3sWeb #type: Valu3sUT
    sleep(1)
    body = web.driver.find_element_by_xpath("//body")
    inner_html = body.get_attribute("innerHTML")
    if(string not in inner_html):
        raise Exception("I should see {}".format(string))

@then('I shouldn\'t see "{string}"')
def i_shouldnt_see(context, string):
    web = context.valu3sWeb #type: Valu3sUT
    body = web.driver.find_element_by_xpath("//body")
    text = body.get_attribute("innerText")
    if string in text:
        raise Exception("I shouldn't see {}".format(string))

@given('a global administrator named "{administrator}"')
def a_global_administrator_named(context, administrator):
    pass

@given("I am on the main page")
def i_am_on_the_main_page(context):
    web = context.valu3sWeb #type: Valu3sUT
    web.driver.get(web.homePage.url)

@given('a method named "{method}" which is public')
def a_method_named_which_is_public(context, method):
    web = context.valu3sWeb #type: Valu3sUT
    web.methodsPage.open()
    web.log_in("administrator", "administrator")
    try:
        m = web.methodsPage.find_method_by_name(method)
        m = web.methodsPage.get_clickable_element_from_method(m)
        m.click()
        try:
            web.loggedInMenu.set_publish_state()
        except(Exception):
            pass
    except:
        web.loggedInMenu.addNew()
        web.loggedInMenu.addNewForm.add_method()
        sleep(1)
        web.loggedInMenu.addNewForm.methodForm.fill_in(method, "summary", "purpose", "description", "strength", "limitation", "reference")
        web.loggedInMenu.addNewForm.methodForm.submit()
        web.loggedInMenu.set_publish_state()


@given('a tool named "{tool}" which is public')
def a_tool_named_which_is_public(context, tool):
    web = context.valu3sWeb #type: Valu3sUT
    web.toolsPage.open()
    web.log_in("administrator", "administrator")
    try:
        t = web.toolsPage.find_tool_by_name(tool)
        t = web.toolsPage.get_clickable_element_from_tool(t)
        t.click()
        try:
            web.loggedInMenu.set_publish_state()
        except(Exception):
            pass
    except:
        web.loggedInMenu.addNew()
        web.loggedInMenu.addNewForm.add_tool()
        sleep(1)
        web.loggedInMenu.addNewForm.toolForm.fill_in(tool, "summary", "purpose", "description", "strength", "limitation", "reference")
        web.loggedInMenu.addNewForm.toolForm.submit()
        web.loggedInMenu.set_publish_state()

@given('a use case named "{use_case}" which is public')
def a_use_case_named_which_is_public(context, use_case):
    web = context.valu3sWeb #type: Valu3sUT
    web.useCasesPage.open()
    web.log_in("administrator", "administrator")
    try:
        uc = web.useCasesPage.find_use_case_by_name(use_case)
        uc = web.useCasesPage.get_clickable_element_from_use_case(uc)
        uc.click()
        try:
            web.loggedInMenu.set_publish_state()
        except(Exception):
            pass
    except:
        web.loggedInMenu.addNew()
        web.loggedInMenu.addNewForm.add_use_case()
        sleep(1)
        web.loggedInMenu.addNewForm.useCaseForm.fill_in(use_case, "summary", "UC1", "a", description="Use case description")
        web.loggedInMenu.addNewForm.useCaseForm.submit()
        web.loggedInMenu.set_publish_state()

@given('a organization named "{organization}" which is public')
def a_organization_named_which_is_public(context, organization):
    web = context.valu3sWeb #type: Valu3sUT
    web.organizationsPage.open()
    web.log_in("administrator", "administrator")
    try:
        o = web.organizationsPage.find_organization_by_name(organization)
        o = web.organizationsPage.get_clickable_element_from_organization(o)
        o.click()
        try:
            web.loggedInMenu.set_publish_state()
        except(Exception):
            pass
    except:
        web.loggedInMenu.addNew()
        web.loggedInMenu.addNewForm.add_organization()
        sleep(1)
        web.loggedInMenu.addNewForm.organizationForm.fill_in(organization, "summary", "acro")
        web.loggedInMenu.addNewForm.organizationForm.submit()
        web.loggedInMenu.set_publish_state()

@given('a standard named "{standard}" which is public')
def a_standard_named_which_is_public(context, standard):
    web = context.valu3sWeb #type: Valu3sUT
    web.standardsPage.open()
    web.log_in("administrator", "administrator")
    try:
        s = web.standardsPage.find_standard_by_name(standard)
        s = web.standardsPage.get_clickable_element_from_standard(s)
        s.click()
        try:
            web.loggedInMenu.set_publish_state()
        except(Exception):
            pass
    except:
        web.loggedInMenu.addNew()
        web.loggedInMenu.addNewForm.add_standard()
        sleep(1)
        web.loggedInMenu.addNewForm.standardForm.fill_in(standard, "summary")
        web.loggedInMenu.addNewForm.standardForm.submit()
        web.loggedInMenu.set_publish_state()


@given('a method named "{method}" which is private')
def a_method_named_which_is_private(context, method):
    web = context.valu3sWeb #type: Valu3sUT
    web.methodsPage.open()
    web.log_in("administrator", "administrator")
    try:
        m = web.methodsPage.find_method_by_name(method)
        m = web.methodsPage.get_clickable_element_from_method(m)
        m.click()
        try:
            web.loggedInMenu.set_private_state()
        except(Exception):
            pass
    except:
        web.loggedInMenu.addNew()
        web.loggedInMenu.addNewForm.add_method()
        sleep(1)
        web.loggedInMenu.addNewForm.methodForm.fill_in(method, "summary", "purpose", "description", "strength", "limitation", "reference")
        web.loggedInMenu.addNewForm.methodForm.submit()
        web.loggedInMenu.set_private_state()

@given('a tool named "{tool}" which is private')
def a_tool_named_which_is_private(context, tool):
    web = context.valu3sWeb #type: Valu3sUT
    web.toolsPage.open()
    web.log_in("administrator", "administrator")
    try:
        t = web.toolsPage.find_tool_by_name(tool)
        t = web.toolsPage.get_clickable_element_from_tool(t)
        t.click()
        try:
            web.loggedInMenu.set_private_state()
        except(Exception):
            pass
    except:
        web.loggedInMenu.addNew()
        web.loggedInMenu.addNewForm.add_tool()
        sleep(1)
        web.loggedInMenu.addNewForm.toolForm.fill_in(tool, "summary", "purpose", "description", "strength", "limitation", "reference")
        web.loggedInMenu.addNewForm.toolForm.submit()
        web.loggedInMenu.set_private_state()

@given('a use case named "{use_case}" which is private')
def a_use_case_named_which_is_private(context, use_case):
    web = context.valu3sWeb #type: Valu3sUT
    web.useCasesPage.open()
    web.log_in("administrator", "administrator")
    try:
        uc = web.useCasesPage.find_use_case_by_name(use_case)
        uc = web.useCasesPage.get_clickable_element_from_use_case(uc)
        uc.click()
        try:
            web.loggedInMenu.set_private_state()
        except(Exception):
            pass
    except:
        web.loggedInMenu.addNew()
        web.loggedInMenu.addNewForm.add_use_case()
        sleep(1)
        web.loggedInMenu.addNewForm.useCaseForm.fill_in(use_case, "summary", "UC1", "a")
        web.loggedInMenu.addNewForm.useCaseForm.submit()
        web.loggedInMenu.set_private_state()

@given('a organization named "{organization}" which is private')
def a_organization_named_which_is_private(context, organization):
    web = context.valu3sWeb #type: Valu3sUT
    web.organizationsPage.open()
    web.log_in("administrator", "administrator")
    try:
        o = web.organizationsPage.find_organization_by_name(organization)
        o = web.organizationsPage.get_clickable_element_from_organization(o)
        o.click()
        try:
            web.loggedInMenu.set_private_state()
        except(Exception):
            pass
    except:
        web.loggedInMenu.addNew()
        web.loggedInMenu.addNewForm.add_organization()
        sleep(1)
        web.loggedInMenu.addNewForm.organizationForm.fill_in(organization, "summary", "acro")
        web.loggedInMenu.addNewForm.organizationForm.submit()
        web.loggedInMenu.set_private_state()

@given('a standard named "{standard}" which is private')
def a_standard_named_which_is_private(context, standard):
    web = context.valu3sWeb #type: Valu3sUT
    web.standardsPage.open()
    web.log_in("administrator", "administrator")
    try:
        s = web.standardsPage.find_standard_by_name(standard)
        s = web.standardsPage.get_clickable_element_from_standard(s)
        s.click()
        try:
            web.loggedInMenu.set_private_state()
        except(Exception):
            pass
    except:
        web.loggedInMenu.addNew()
        web.loggedInMenu.addNewForm.add_standard()
        sleep(1)
        web.loggedInMenu.addNewForm.standardForm.fill_in(standard, "summary")
        web.loggedInMenu.addNewForm.standardForm.submit()
        web.loggedInMenu.set_private_state()


@given("Exists method related-method1")
def exists_method_related_method_1(context):
    a_method_named_which_is_public(context, "related-method1")

@given("Exists method related-method2")
def exists_method_related_method_2(context):
    a_method_named_which_is_public(context, "related-method2")

@given("Exists method related-method3")
def exists_method_related_method_3(context):
    a_method_named_which_is_public(context, "related-method3")

@given("Exists standard my-standard1")
def exists_standard_my_standard_1(context):
    a_standard_named_which_is_public(context, "my-standard1")

@given("Exists standard my-standard2")
def exists_standard_my_standard_2(context):
    a_standard_named_which_is_public(context, "my-standard2")

@given("Exists standard my-standard3")
def exists_standard_my_standard_3(context):
    a_standard_named_which_is_public(context, "my-standard3")


@when('I go to "{post}"')
def i_go_to_post(context, post):
    pass


@then('I can see "{post}"')
def i_can_see_post(context, post):
    pass

def exists_evaluation_scenario_named(context, name):
    web = context.valu3sWeb #type: Valu3sUT
    web.homePage.open()
    web.log_in("administrator", "administrator")
    try:
        es = web.homePage.get_evaluation_scenario_by_name(name)
        es = web.homePage.get_clickable_element_from_element(es)
        es.click()
        try:
            web.loggedInMenu.set_publish_state()
        except(Exception):
            pass
    except:
        web.loggedInMenu.addNew()
        web.loggedInMenu.addNewForm.add_evaluation_scenario()
        sleep(1)
        web.loggedInMenu.addNewForm.evaluationScenarioForm.fill_in(name, "summary", "ID111", "TextualDescription", "1")
        web.loggedInMenu.addNewForm.evaluationScenarioForm.submit()
        web.loggedInMenu.set_publish_state()

def exists_test_case_named(context, name):
    web = context.valu3sWeb #type: Valu3sUT
    web.homePage.open()
    web.log_in("administrator", "administrator")
    try:
        tc = web.homePage.get_testcase_by_name(name)
        tc = web.homePage.get_clickable_element_from_element(tc)
        tc.click()
        try:
            web.loggedInMenu.set_publish_state()
        except(Exception):
            pass
    except:
        web.loggedInMenu.addNew()
        web.loggedInMenu.addNewForm.add_test_case()
        sleep(1)
        web.loggedInMenu.addNewForm.testCaseForm.fill_in(name, "summary", "TC111", "F", "", "Component1")
        web.loggedInMenu.addNewForm.testCaseForm.submit()
        web.loggedInMenu.set_publish_state()

def exists_requirement_named(context, name):
    web = context.valu3sWeb #type: Valu3sUT
    web.homePage.open()
    web.log_in("administrator", "administrator")
    try:
        r = web.homePage.get_requirement_by_name(name)
        r = web.homePage.get_clickable_element_from_element(r)
        r.click()
        try:
            web.loggedInMenu.set_publish_state()
        except(Exception):
            pass
    except:
        web.loggedInMenu.addNew()
        web.loggedInMenu.addNewForm.add_requirement()
        sleep(1)
        web.loggedInMenu.addNewForm.requirementForm.fill_in(name, "summary", "ID111", "textualDescription")
        web.loggedInMenu.addNewForm.requirementForm.submit()
        web.loggedInMenu.set_publish_state()

def check_list(list1, list2):
    for item1 in list1:
        if item1 in list2:
            return True
        else:
            return False
    return True