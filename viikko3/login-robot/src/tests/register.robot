*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  abc  abcd1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  5678efgh
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input Credentials  ka  k1j2h3u4y5
    Output Should Contain  Username invalid

Register With Valid Username And Too Short Password
    Input Credentials  mauno  k1k2k3k
    Output Should Contain  Password invalid

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  mauno  salasana
    Output Should Contain  Password invalid

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command