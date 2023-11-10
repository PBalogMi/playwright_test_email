Feature: Verify Gmail account functionality with the FireFox web browser

  Scenario Outline: The block level 1 - verify login/logout functionality
    Given Google's "Sign in" page is displayed
    When the login name is filled out with the email address "<email>"
    Then the password on the second page is filled out with "<password>"
    And execute the login into the email
    Then the user clicks Google account with the name "<account_name>" and then the logout button
    And execute logout

    Examples:
      | email              | password   | account_name |
      | pbalogmi@gmail.com | ***        | Peter Balog  |

  Scenario Outline: The block level 2 - send an email to the address picked from the contact list
    Given Google's "Sign in" page is displayed
    When the login name is filled out with the email address "<email>"
    Then the password on the second page is filled out with "<password>"
    And execute the login into the email
    Then pick up the name "<name_from_contacts>" with email address "<email_address_from_contacts>" from contacts
    And send email
    Then the user clicks Google account with the name "<account_name>" and then the logout button
    And execute logout

    Examples:
      | email              | password   | account_name | name_from_contacts | email_address_from_contacts |
      | pbalogmi@gmail.com | ***        | Peter Balog  | Peter Balog        | pbalogmi@gmail.com          |

  Scenario Outline: The block level 3 - send an email to the address picked from the contact list with an attachment
    Given Google's "Sign in" page is displayed
    When the login name is filled out with the email address "<email>"
    Then the password on the second page is filled out with "<password>"
    And execute the login into the email
    Then pick up the name "<name_from_contacts>" with email address "<email_address_from_contacts>" from contacts
    And send an email with an attached file named funny_picture.png
    Then the user clicks Google account with the name "<account_name>" and then the logout button
    And execute logout

    Examples:
      | email              | password   | account_name | name_from_contacts | email_address_from_contacts |
      | pbalogmi@gmail.com | ***        | Peter Balog  | Peter Balog        | pbalogmi@gmail.com          |
