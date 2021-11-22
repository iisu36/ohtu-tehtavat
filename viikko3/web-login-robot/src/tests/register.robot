*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  mauno
    Set Password  mauno456
    Set Password Confirmation  mauno456
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ma
    Set Password  mauno6789
    Set Password Confirmation  mauno6789
    Submit Credentials
    Register Should Fail With Message  Username invalid

Register With Valid Username And Too Short Password
    Set Username  mauno
    Set Password  mauno67
    Set Password Confirmation  mauno67
    Submit Credentials
    Register Should Fail With Message  Password invalid

Register With Nonmatching Password And Password Confirmation
    Set Username  mauno
    Set Password  mauno6789
    Set Password Confirmation  mauno678
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Register Successfully
    Go To Login Page
    Login Successfully
    Login Should Succeed

Login After Failed Registration
    Register Failing
    Go To Login Page
    Login Failing
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Reset Application And Go To Register Page
    Reset Application
    Go To Register Page

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}