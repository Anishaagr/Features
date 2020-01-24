from behave import given, when, then
from features.steps.step_imp_context_search import *
import allure

expected_error_message = """The selected Country(s) 'Argentina", "Austria", "Belgium", "Canada", "Chile", "China' may not be valid for your current Appliance Model and/or Version selection."""


@when('Select Appliance Model "{model_no}" from Appliance Model drop-down')
def step_impl(context, model_no):
    """This test step will select Appliance Model """
    select_appliance_model(model_no)


@then('Get list of Country for "{model_no}" appliance model')
def step_imp(context, model_no):
    """This test step will fetch the values displayed in Country drop-down"""
    count = click_on_country_drop_down_for_appliance_model(model_no)
    assert len(count) == 0, "Country list verification failed"


@when('Select Version "{version}" from Version drop-down')
def step_impl(context, version):
    """This test step will select version"""
    select_version(version)


@then('Verify "{drop_down}" drop-down has no values')
def step_impl(context, drop_down):
    """This test step will verify, secondary drop-downs have no values, if the primary filters do nat have data
    related"""
    values_in_drop_down = verify_context_search_for_secondary_drop_down_filters(drop_down)
    assert values_in_drop_down == 0, f"{drop_down} drop-down is not empty"


@when('Select 1st "{count}" countries from Country drop-down')
def step_impl(context, count):
    """This test step will select no. of values from Country drop-down """
    select_countries(count)
    print("Select 1st eight countries from Country drop-down")


@then('Verify error indicator over Country drop-down')
def step_impl(context):
    """This test step will verify error indicator is generated for invalid selections as per primary filters"""
    error_message = error_indicator()
    print("returned error message is  :    ", '\n', error_message)
    assert error_message == expected_error_message, "error message is not displayed"
