*** Settings ***
Library    SeleniumLibrary

*** Variables ***


*** Test Cases ***
LoginTest
    Open Browser    https://automationteststore.com/    chrome
    Maximize Browser Window
    Click Link    xpath://a[normalize-space()='Login or register']
    Input Text    id:loginFrm_loginname    Test_Website
    Input Text    id:loginFrm_password    saba70/8
    Click Element    xpath:(//button[normalize-space()='Login'])[1]
    Close Browser

*** Keywords ***
