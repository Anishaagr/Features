from features.steps.step_imp_context_search import webdriver_shutdown, cortex_ui_page, add_filters, clear_selected, navigate_to_advance_serach_page

URL = "http://localhost:4201/"


def before_feature(context, feature):
    if "Context Search between primary filters and secondary drop-down filters" in str(feature):
        cortex_ui_page(URL)


def before_scenario(context, scenario):
    if "Select Appliance model 3340 and verify context search in Country drop-down filter" in str(scenario):
        navigate_to_advance_serach_page()
        add_filters()


def before_step(context, step):
    if 'Select 1st "8" countries from Country drop-down' in str(step):
        clear_selected("Version")
        clear_selected("Appliance Model")


def after_feature(context, feature):
    if "Context Search between primary filters and secondary drop-down filters" in str(feature):
        webdriver_shutdown()

