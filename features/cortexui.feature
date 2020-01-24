Feature: Context Search between primary filters and secondary drop-down filters
  Scenario: Select Appliance model 3340 and verify context search in Country drop-down filter
    When Select Appliance Model "5220" from Appliance Model drop-down
    Then Get list of Country for "5220" appliance model
    When Select Appliance Model "3340" from Appliance Model drop-down
    Then Get list of Country for "3340" appliance model

  Scenario: Select Appliance model "3340" and version "2.7.1" and verify context search in Country, State, City,
            Account Name and Hostname  drop-down filter
    When Select Appliance Model "3340" from Appliance Model drop-down
    When Select Version "2.7.1" from Version drop-down
    Then Verify "Country" drop-down has no values
    And Verify "State" drop-down has no values
    And Verify "City" drop-down has no values
    And Verify "Account Name" drop-down has no values
    And Verify "Hostname" drop-down has no values

  Scenario: Select 1st eight countries, then select appliance model 3340, error indicator is displayed on country
            drop-down
    When Select 1st "8" countries from Country drop-down
    And Select Appliance Model "3340" from Appliance Model drop-down
    Then Verify error indicator over Country drop-down