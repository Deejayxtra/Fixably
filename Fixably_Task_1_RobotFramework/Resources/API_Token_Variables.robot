*** Settings ***
Documentation    Obtain an API token using the /token endpoint
Library          RequestsLibrary
Library          Collections
Library          JSONLibrary


*** Variables ***
${base_url}     https://careers-api.fixably.com/
${Code}         34962787
