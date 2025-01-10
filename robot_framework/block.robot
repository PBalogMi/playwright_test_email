*** Settings ***
Library    Browser
Library    ../src/get_password.py


*** Variables ***
${BROWSER}      Firefox
${HEADLESS}     false
${BASE_URL}     https://gmail.com
${ACCOUNT_NAME}     Peter Balog
${EMAIL}        pbalogmi@gmail.com


*** Test Cases ***
Login/Logout
    Open Google's "Sign in" page
    the login name is filled out with the email address
    the password on the second page is populated using the password stored in the "config.env" file
    execute the login into the email
    the user clicks Google account labeled Peter Balog
    the user clicks the logout button


*** Keywords ***
Open Google's "Sign in" page
    new browser    ${BROWSER}   headless=${HEADLESS}
    set browser timeout    45
    new page    ${BASE_URL}     commit

the login name is filled out with the email address
    type text    css=#identifierId      ${EMAIL}
    click    id=identifierNext

the password on the second page is populated using the password stored in the "config.env" file
    ${password}=     Get Password From Env
    type text   xpath=//input[@type='password' and @name='Passwd']      ${password}

execute the login into the email
    click   id=passwordNext

the user clicks Google account labeled Peter Balog
    ${account_element}=     get element by     Label     Google Account: ${ACCOUNT_NAME}\n(${EMAIL})
    click    ${account_element}

the user clicks the logout button
    ${account}=     set selector prefix    iframe[name='account'] >>>
    ${click_sign_out}=     get element by role    link    name=Sign out
    click   ${click_sign_out}
    set selector prefix    ${account}
