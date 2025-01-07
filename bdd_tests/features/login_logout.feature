Feature: Verify login/logout Gmail account functionality with the FireFox web browser

  Scenario Outline: Verify login functionality - level 1
    Given Google's "Sign in" page is displayed by FireFox web browser
    When the login name is filled out with the email address "<email>"
    And the password on the second page is populated using the password stored in the "config.env" file
    Then execute the login into the email

    Examples:
      | email              |
      | pbalogmi@gmail.com |

  Scenario Outline: Verify logout functionality - level 1
    When the user clicks the Google account with the name "<account_name>"
    Then execute logout

    Examples:
      | account_name |
      | Peter Balog  |
