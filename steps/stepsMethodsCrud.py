from behave import *
from stepsCommon import *

@given("creating-method-1 has")
def creating_method_1_has(context):
    related_methods = []
    for row in context.table:
        related_methods.append(row['related-method'])
        context.types[row['related-method']] = "method"

    context.datas["related-methods"] = related_methods

@given("Exists tool my-tool1")
def exists_tool_my_tool1(context):
    a_tool_named_which_is_public(context, "my-tool1")

@given("Exists tool my-tool2")
def exists_tool_my_tool2(context):
    a_tool_named_which_is_public(context, "my-tool2")

@given("Exists tool my-tool3")
def exists_tool_my_tool3(context):
    a_tool_named_which_is_public(context, "my-tool3")

@given("Exists part method my-part-method1")
def exists_part_method_my_part_method1(context):
    a_method_named_which_is_public(context, "my-part-method1")

@given("Exists part method my-part-method2")
def exists_part_method_my_part_method2(context):
    a_method_named_which_is_public(context, "my-part-method2")

@given("Exists part method my-part-method3")
def exists_part_method_my_part_method3(context):
    a_method_named_which_is_public(context, "my-part-method3")

@given("Exists VV method named my-use-case1")
def exists_vv_method_named_my_use_case1(context):
    a_use_case_named_which_is_public(context, "my-use-case1")

@given("Exists VV method named my-use-case2")
def exists_vv_method_named_my_use_case2(context):
    a_use_case_named_which_is_public(context, "my-use-case2")

@given("Exists VV method named my-use-case3")
def exists_vv_method_named_my_use_case3(context):
    a_use_case_named_which_is_public(context, "my-use-case3")

@when("I try to create creating-method1")
def i_try_to_create_creating_method1(context):
    web = context.valu3sWeb#type: Valu3sUT
    web.homePage.open()
    web.loggedInMenu.addNewForm.add_method()
    sleep(1)
    web.loggedInMenu.addNewForm.methodForm.fill_in("creating-method1", "", "purpose", "description", "strengths", "limitations", "references", context.datas["related-methods"])

@then("I should see creating-method-1 with")
def i_should_see_creating_method_1_with(context):
    web = context.valu3sWeb#type: Valu3sUT
    relatedMethods = []
    for row in context.table:
        type = ""
        try:
            type = context.types[row['see-item']]
        except(Exception):
            pass
        if(type == "method"):
            relatedMethods.append(row['see-item'])
    mp = SingleMethodPageUT(web.driver, "")

    if not check_list(relatedMethods, [a.get_attribute("innerText") for a in mp.get_related_methods()]):
        raise Exception("I should see creating-method-1 with")

    if("creating-method1" not in mp.get_title_content()):
        raise Exception("I should see creating-method-1 with")
    if("purpose" not in mp.get_purpose_content()):
        raise Exception("I should see creating-method-1 with")
    if("description" not in mp.get_description_content()):
        raise Exception("I should see creating-method-1 with")
    if("strengths" not in mp.get_strengths_content()):
        raise Exception("I should see creating-method-1 with")
    if("limitations" not in mp.get_limitations_content()):
        raise Exception("I should see creating-method-1 with")
    if("references" not in mp.get_references_content()):
        raise Exception("I should see creating-method-1 with")
    

@given("There already exists creating-method-1")
def there_already_exists_creating_method_1(context):
    web = context.valu3sWeb#type: Valu3sUT
    web.methodsPage.open()
    web.log_in("administrator", "administrator")

    try:
        web.methodsPage.find_method_by_name("creating-method-1")
    except(Exception):
        i_try_to_create_creating_method1(context)

@when("I add related methods to method")
def i_add_related_methods_to_method(context):
    relatedMethods = []
    for row in context.table:
        relatedMethods.append(row["related-method"])

    web = context.valu3sWeb#type: Valu3sUT
    web.methodsPage.open()
    method = web.methodsPage.find_method_by_name("creating-method-1")
    el = web.methodsPage.get_clickable_element_from_method(method)
    web.driver.execute_script("arguments[0].click()", el)
    sleep(1)
    web.loggedInMenu.edit()
    web.loggedInMenu.addNewForm.methodForm.fill_in("", relatedMethods=relatedMethods)

@then("I should find creating-method-1 with")
def i_should_find_creating_method_1_with(context):
    web = context.valu3sWeb#type: Valu3sUT
    web.methodsPage.open()
    method = web.methodsPage.find_method_by_name("creating-method-1")
    el = web.methodsPage.get_clickable_element_from_method(method)
    web.driver.execute_script("arguments[0].click()", el)
    sleep(1)
    i_should_see_creating_method_1_with(context)

@when("I add standards to method")
def i_add_standard_to_method(context):
    standards = []
    for row in context.table:
        standards.append(row["standard"])

    web = context.valu3sWeb#type: Valu3sUT
    web.methodsPage.open()
    method = web.methodsPage.find_method_by_name("creating-method-1")
    el = web.methodsPage.get_clickable_element_from_method(method)
    web.driver.execute_script("arguments[0].click()", el)
    sleep(1)
    web.loggedInMenu.edit()
    web.loggedInMenu.addNewForm.methodForm.fill_in("", standards=standards)

@when("I add tools to method")
def i_add_tools_to_method(context):
    tools = []
    for row in context.table:
        tools.append(row["tool"])

    web = context.valu3sWeb#type: Valu3sUT
    web.methodsPage.open()
    method = web.methodsPage.find_method_by_name("creating-method-1")
    el = web.methodsPage.get_clickable_element_from_method(method)
    web.driver.execute_script("arguments[0].click()", el)
    sleep(1)
    web.loggedInMenu.edit()
    web.loggedInMenu.addNewForm.methodForm.fill_in("", tools=tools)

@when("I add part-methods to method")
def i_add_part_methods_to_method(context):
    partMethods = []
    for row in context.table:
        partMethods.append(row["part-method"])

    web = context.valu3sWeb#type: Valu3sUT
    web.methodsPage.open()
    method = web.methodsPage.find_method_by_name("creating-method-1")
    el = web.methodsPage.get_clickable_element_from_method(method)
    web.driver.execute_script("arguments[0].click()", el)
    sleep(1)
    web.loggedInMenu.edit()
    web.loggedInMenu.addNewForm.methodForm.fill_in("", partMethods=partMethods)

@when("I add use cases to method")
def i_add_use_cases_to_method(context):
    useCases = []
    for row in context.table:
        useCases.append(row["use-case"])

    web = context.valu3sWeb#type: Valu3sUT
    web.methodsPage.open()
    method = web.methodsPage.find_method_by_name("creating-method-1")
    el = web.methodsPage.get_clickable_element_from_method(method)
    web.driver.execute_script("arguments[0].click()", el)
    sleep(1)
    web.loggedInMenu.edit()
    web.loggedInMenu.addNewForm.methodForm.fill_in("", useCases=useCases)

@when("I remove creating-method-1")
def i_remove_creating_method_1(context):
    web = context.valu3sWeb#type: Valu3sUT
    web.methodsPage.open()
    method = web.methodsPage.find_method_by_name("creating-method-1")
    el = web.methodsPage.get_clickable_element_from_method(method)
    web.driver.execute_script("arguments[0].click()", el)
    sleep(1)
    web.loggedInMenu.actions()
    web.loggedInMenu.actionsForm.delete()

@then("I shouldn't find creating-method-1")
def i_shouldnt_find_creating_method_1(context):
    web = context.valu3sWeb#type: Valu3sUT
    web.methodsPage.open()
    try:
        web.methodsPage.find_method_by_name("creating-method-1")
        raise Exception("I shouldn't find creating-method-1")
    except(Exception):
        pass