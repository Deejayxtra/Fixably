*** Settings ***
Documentation    Obtain an API token using the /token endpoint
Library          RequestsLibrary
#Library          ExtendedRequestsLibrary
Library          BuiltIn
Library          String
Library          Collections
Library          JSONLibrary
Resource         ../resources/API_Token_Variables.robot



*** Keywords ***
Obtain an API token
    [Tags]  Token
    create session  API_Token   ${base_url}
    ${Data}=        create dictionary   Code=${Code}
    ${response}=    post on session     API_Token   /token      data=${Data}
    ${Token}=       evaluate            $response.json().get("token")
    log to console  ${response.status_code}
    log to console  ${response.content}

    #Validations
    ${status_code}=     convert to string   ${response.status_code}
    should be equal     ${status_code}      200


