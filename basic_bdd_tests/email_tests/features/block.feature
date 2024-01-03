Feature: Verify Gmail account functionality with the FireFox web browser

  Scenario Outline: The block level 1 - verify login/logout functionality
    Given Google's "Sign in" page is displayed
    When the login name is filled out with the email address "<email>"
    And the password on the second page is populated using the password stored in the "config.env" file
    Then execute the login into the email
    When the user clicks Google account labeled "<account_name>"
    Then the user clicks the logout button

    Examples:
      | email              | account_name |
      | pbalogmi@gmail.com | Peter Balog  |

  Scenario Outline: The block level 2 - send an email to the address picked from the contact list
    Given Google's "Sign in" page is displayed
    When the login name is filled out with the email address "<email>"
    And the password on the second page is populated using the password stored in the "config.env" file
    Then execute the login into the email
    When pick up the name "<name_from_contacts>" with email address "<email_address_from_contacts>" from contacts
    Then send email
    When the user clicks Google account labeled "<account_name>"
    Then the user clicks the logout button

    Examples:
      | email              | account_name | name_from_contacts | email_address_from_contacts |
      | pbalogmi@gmail.com | Peter Balog  | Peter Balog        | pbalogmi@gmail.com          |

  Scenario Outline: The block level 3 - send an email to the address picked from the contact list with an attachment
    Given Google's "Sign in" page is displayed
    When the login name is filled out with the email address "<email>"
    And the password on the second page is populated using the password stored in the "config.env" file
    Then execute the login into the email
    When pick up the name "<name_from_contacts>" with email address "<email_address_from_contacts>" from contacts
    Then send an email with an attached file named funny_picture.png
    When the user clicks Google account labeled "<account_name>"
    Then the user clicks the logout button

    Examples:
      | email              | account_name | name_from_contacts | email_address_from_contacts |
      | pbalogmi@gmail.com | Peter Balog  | Peter Balog        | pbalogmi@gmail.com          |
