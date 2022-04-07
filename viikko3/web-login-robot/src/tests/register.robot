*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Open Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  testi
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  testi
    Set Password  test123
    Set Password Confirmation  test123
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  testi
    Set Password  testi123
    Set Password Confirmation  testi1234
    Submit Credentials
    Register Should Fail With Message  Passwords must be match

*** Keywords ***
Register Should Succeed
    Home Page After Registeing Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Open Register Page
    Go To Register Page
    Register Page Should Be Open
    