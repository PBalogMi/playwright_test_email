Feature: Verify the Gmail account functionality to send email to the address picked from the contact list with FireFox web browser

  Scenario Outline: Send an email to the address picked from the contact list - level 2
    Given Google's "Sign in" page is displayed, system will automatically login into account based on credentials from level 1
    When you are already logged in the Google account
    And the name "<name_from_contacts>" with email address "<email_address_from_contacts>" is picked up from contacts
    Then send email

    Examples:
      | name_from_contacts | email_address_from_contacts |
      | Peter Balog        | pbalogmi@gmail.com          |

  Scenario: Send an email to the address picked from the contact list with an attachment - level 3
    When you are already logged in the Google account
    And the name and email address from contacts are already given from level 2 - Examples table
    Then attach file named as funny_picture.png
    And send email
    And the user clicks the Google account with the account name from level 1 and then the logout button
