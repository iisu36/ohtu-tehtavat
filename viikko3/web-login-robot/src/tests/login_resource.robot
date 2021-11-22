*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${USERNAME}  mauno
${PASSWORD}  mauno1234
${FAIL_USERNAME}  mauno
${FAIL_PASSWORD}  mauno

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Successfully
    Set Username  ${USERNAME}
    Set Password  ${PASSWORD}
    Set Password Confirmation  ${PASSWORD}
    Click Button  Register

Login Successfully
    Set Username  ${USERNAME}
    Set Password  ${PASSWORD}
    Click Button  Login

Register Failing
    Set Username  ${FAIL_USERNAME}
    Set Password  ${FAIL_PASSWORD}
    Set Password Confirmation  ${FAIL_PASSWORD}
    Click Button  Register

Login Failing
    Set Username  ${FAIL_USERNAME}
    Set Password  ${FAIL_PASSWORD}
    Click Button  Login