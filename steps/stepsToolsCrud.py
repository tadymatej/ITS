from behave import *
from stepsCommon import *

#TODO data from table
@given("creating-tool1 has")
def creating_tool_1_has(context):
    pass

@given("Exists test case my-test-case1")
def exists_test_case_my_test_case1(context):
    exists_test_case_named(context, "my-test-case1")

@given("Exists test case my-test-case2")
def exists_test_case_my_test_case2(context):
    exists_test_case_named(context, "my-test-case2")

@given("Exists test case my-test-case3")
def exists_test_case_my_test_case3(context):
    exists_test_case_named(context, "my-test-case3")

@when("I create creating-tool1")
def i_create_creating_tool_1(context):
    pass

#TODO data from table
@then("I should find tool creating-tool1 with")
def i_should_find_tool_creating_tool_1_with(context):
    pass

@given("There already exists tool creating-tool1")
def there_already_exists_tool_creating_tool_1(context):
    pass

#TODO: data from table
@when("I add related methods to tool")
def i_add_related_methods_to_tool(context):
    pass

#TODO data from table
@when("I add test cases to tool")
def i_add_test_cases_to_tool(context):
    pass

#TODO data from table
@when("I add standards to tool")
def i_add_standards_to_tool(context):
    pass

@when("I remove tool creating-tool1")
def i_remove_tool_creating_tool_1(context):
    pass

@then("I shouldn't find tool creating-tool1")
def t_shouldnt_find_tool_creating_tool1(context):
    pass