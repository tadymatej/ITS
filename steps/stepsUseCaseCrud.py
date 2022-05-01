from behave import *

from stepsCommon import *

#TODO data from table
@given("creating-use-case1 has")
def creating_use_case1_has(context):
    pass

@given("Exists organization my-organization1")
def exists_organization_my_organization1(context):
    a_organization_named_which_is_private(context, "my-organization1")

@given("Exists organization my-organization2")
def exists_organization_my_organization2(context):
    a_organization_named_which_is_private(context, "my-organization2")

@given("Exists organization my-organization3")
def exists_organization_my_organization3(context):
    a_organization_named_which_is_private(context, "my-organization3")


@given("Exists evaluation scenario my-evaluation-scenario1")
def exists_evaluation_scenario_my_evaluation_scenario1(context):
    exists_evaluation_scenario_named(context, "my-evaluation-scenario1")

@given("Exists evaluation scenario my-evaluation-scenario2")
def exists_evaluation_scenario_my_evaluation_scenario2(context):
    exists_evaluation_scenario_named(context, "my-evaluation-scenario2")

@given("Exists evaluation scenario my-evaluation-scenario3")
def exists_evaluation_scenario_my_evaluation_scenario3(context):
    exists_evaluation_scenario_named(context, "my-evaluation-scenario3")


@when('I create use case creating-use-case1 with case domain "{domain}"')
def i_create_use_case_creating_use_case1_with_case_domain(context, domain):
    pass

@then('I should see use case domain "{domain}"')
def i_should_see_use_case_domain(context, domain):
    pass

@then('I should see evaluation scenarios list with "{item}"')
def i_should_see_evaluation_scenarios_list_with(context, item):
    pass

@then("I should see use case provider my-organization1")
def i_should_see_use_case_provider_my_organization1(context):
    pass

@given('I have already created use case with case domain "{domain}"')
def i_have_already_created_use_case_with_case_domain(context, domain):
    pass

@when('I change case domain to "{domain}"')
def i_change_case_domain_to(context, domain):
    pass

@then('I should see case domain "{domain}"')
def i_should_see_case_domain(context, domain):
    pass

@given('I have created use case creating-use-case1 with case domain "{domain}"')
def i_have_created_use_case_creating_use_case1_with_case_domain(context, domain):
    pass

#TODO data from table
@when("I add evaluation scenarios")
def i_add_evaluation_scenarios(context):
    pass

#TODO data from table
@then("I should see use case creating-use-case1 with evaluation scenarios list with")
def i_should_see_use_case_creating_use_case1_with_evaluation_scenarios_list_with(context):
    pass

#TODO data from table
@when("I add standards")
def i_add_standards(context):
    pass

#TODO data from table
@then("I should see use case creating-use-case1 with standards")
def i_should_see_use_case_creating_use_case1_with_standards(context):
    pass

#TODO data from table
@when("I add partners")
def i_add_partners(context):
    pass

#TODO data from table
@then("I should see use case creating-use-case1 with partners")
def i_should_see_use_case_creating_use_case1_with_partners(context):
    pass

@when("I delete creating-use-case1")
def i_delete_creating_use_case1(context):
    pass

@then("There shouldn't be creating-use-case1")
def there_shouldnt_be_creating_use_case1(context):
    pass