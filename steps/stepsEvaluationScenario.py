from behave import *
from stepsCommon import *

#TODO parameter from table
@given("creating-evaluation-scenario has")
def creating_evaluation_scenarion_has(context):
    pass

@given("Exists use case named my-use-case1")
def exists_use_case_named_my_use_case1(context):
    a_use_case_named_which_is_public(context, "my-use-case1")

@given("Exists requirement named my-requirement1")
def exists_requirement_named_my_requirement1(context):
    exists_requirement_named(context, "my-requirement1")

@given("Exists requirement named my-requirement2")
def exists_requirement_named_my_requirement2(context):
    exists_requirement_named(context, "my-requirement2")

@given("Exists requirement named my-requirement3")
def exists_requirement_named_my_requirement3(context):
    exists_requirement_named(context, "my-requirement3")

@given("Exists VV method named my-VV-method1")
def exists_vv_method_named_my_vv_method1(context):
    a_method_named_which_is_public(context, "VV-method1")

@given("Exists VV method named my-VV-method2")
def exists_vv_method_named_my_vv_method2(context):
    a_method_named_which_is_public(context, "VV-method2")

@given("Exists VV method named my-VV-method3")
def exists_vv_method_named_my_vv_method3(context):
    a_method_named_which_is_public(context, "VV-method3")

#TODO parameter from table
@when("I create a new evaluation scenario with")
def i_create_a_new_ecaluation_scenarion_with(context):
    pass

#TODO: parameter from table
@then("I should see evaluation with")
def i_should_see_evaluation_with(context):
    pass

@given("I have created evaluation scenario creating-evaluation-scenario")
def i_have_created_evaluation_scenario_creating_evaluation_scenario(context):
    pass

#TODO: parameter from table
@when("I add evaluation scenario requirements")
def i_add_evaluation_scenario_requirements(context):
    pass

#TODO parameter from table
@then("I should see evaluation creating-evaluation-scenario with")
def i_should_see_evaluation_creating_evaluation_scenarion_with(context):
    pass

#TODO parameters from table
@when("I add evaluation scenario VV methods")
def i_add_evaluation_scenario_vv_methods(context):
    pass

@when("I remove creating-evaluation-scenario")
def i_remove_creating_evaluation_scenario(context):
    pass

@then("There shouldn't be creating-evaluation-scenario")
def there_shouldnt_be_creating_evaluation_scenario(context):
    pass