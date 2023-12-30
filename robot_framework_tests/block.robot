*** Settings ***
Library    Browser





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
    the password on the second page is filled out with password
    execute the login into the email
    the user clicks Google account labeled Peter Balog
    the user clicks the logout button

*** Keywords ***
Open Google's "Sign in" page
    new browser    ${BROWSER}   headless=${HEADLESS}
    set browser timeout    45
    new page    ${BASE_URL}     commit

the login name is filled out with the email address
    type text    css=#identifierId      pbalogmi@gmail.com
    click    id=identifierNext

the password on the second page is filled out with password
    type text   xpath=//input[@type='password' and @name='Passwd']      ***

execute the login into the email
    click   id=passwordNext

the user clicks Google account labeled Peter Balog
    click    xpath=//html/body/div[7]/div[3]/div/div[1]/div/div[2]/div[2]/header/div[2]/div[3]/div[1]/div[2]/div/a
    #${account_element}=     get element by    Label     Google Account: ${ACCOUNT_NAME}    \n(${EMAIL})
    #get element by    ${account_element}
    #${frame}=    get element    iframe[name='account']
    #switch page    ${frame}

the user clicks the logout button
    # click     id=SignOut
    # click       xpath=//[@name='Sign out']
    # click with options        xpath=//[@name='Sign out']
    ${sign_out_element}    get element by role    link      name=Sign out
    click   ${sign_out_element}     click with options    BUTTON_LEFT


