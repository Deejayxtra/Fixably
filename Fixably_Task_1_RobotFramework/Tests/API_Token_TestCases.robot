*** Settings ***
Documentation    Obtain an API token using the /token endpoint
Library          RequestsLibrary
Library          Collections
Library          JSONLibrary
Resource         ../resources/API_Token_Variables.robot
Resource         ../resources/API_Token_Keywords.robot




*** Test Cases ***
Fixably API Documentation
    Obtain an API token
