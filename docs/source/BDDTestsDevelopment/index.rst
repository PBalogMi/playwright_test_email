BDD tests development
=====================

Gherkin: The Language of Behavior
---------------------------------

Core Concepts:

Feature: Represents a high-level user story or requirement.
    - Example: Feature: Login Functionality

Scenario: A specific example or use case within a feature.
    - Example: Scenario: Successful Login

Steps: Individual actions or assertions within a scenario.
     - Uses keywords like:
        - Given: Establishes the initial context or preconditions.
        - When: Describes the action or event that triggers a change in the system.
        - Then: Specifies the expected outcome or result.
        - And/But: Used to continue a step within the same Given, When, or Then block.
    - Example:

        .. code:: gherkin

            Feature: Login Functionality

            Scenario: Successful Login
                Given I am on the login page
                When I enter valid username and password
                Then I should be logged in successfully

            Scenario: Unsuccessful Login
                Given I am on the login page
                When I enter invalid credentials
                Then I should see an error message

pytest-bdd: Bridging Gherkin and Python
---------------------------------------

How it Works:

Parsing: pytest-bdd parses the Gherkin feature files, extracting the scenarios and individual steps.
Mapping: It maps each Gherkin step to a corresponding Python function (step definition).
Execution: During test execution, pytest-bdd executes the Python functions associated with each step in the defined order.
Key Components:

@given, @when, @then: These decorators in Python are used to define step definitions. They correspond to the respective Gherkin keywords.
@scenario: This decorator links a Python test function to a specific scenario in a feature file.

Example:

.. code:: python

    from pytest_bdd import given, when, then, scenario

    @given('I am on the login page')
    def on_login_page(browser):
        browser.get("https://example.com/login")

    @when('I enter valid username and password')
    def enter_credentials(browser, username, password):
        browser.fill('input[name="username"]', username)
        browser.fill('input[name="password"]', password)
        browser.find_element_by_css_selector('button[type="submit"]').click()

    @then('I should be logged in successfully')
    def verify_login_success(browser):
        assert "Welcome" in browser.page_source

    @scenario('login.feature', 'Successful Login') 
    def test_successful_login(): 
        pass

Benefits of pytest-bdd
----------------------

Improved Readability: Gherkin provides a clear and concise way to describe test scenarios, making them easier to understand for both technical and non-technical stakeholders.

Collaboration: Fosters better collaboration between developers, testers, and business analysts by using a shared language.

Maintainability: Tests become more maintainable as changes in requirements can be easily reflected in the Gherkin scenarios.

Reusability: Step definitions can be reused across multiple scenarios, reducing code duplication.

Key Considerations
------------------

Feature File Structure: Organize feature files into a clear and maintainable structure within your project.

Step Definition Naming: Use clear and descriptive names for your step definition functions.

Data-Driven Testing: Use data tables within Gherkin scenarios to test different sets of input data.

Regular Maintenance: Keep your feature files and step definitions up-to-date as your application evolves.

By effectively utilizing pytest-bdd and Gherkin, you can enhance the quality and maintainability of your tests while improving communication and collaboration within your development team.