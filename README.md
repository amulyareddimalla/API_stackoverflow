
# API Automation Stackoverflow API

This is an API Automation script using Python Requests Library 


## Test Cases
1) Create an account in "StackApps" to get unique 'Client ID', 'Client Secret Key'
2) POST "https://stackoverflow.com/oauth" along with Query Params (Client ID, Scope, Redirect URI) to generate the Code
3) POST "https://stackoverflow.com/oauth/access_token/json" with BODY (URL Encoded) having params (Client ID, client Secret, Code, redirect URI) to generate Access_Token in JSON Response
4) Function to Test Badfes API's with 
---Badges having ID 'https://api.stackexchange.com/2.3/badges/1;2', 

---Badges with Recipients 'https://api.stackexchange.com/2.3/badges?recipients=12345' and 

---Badges by Tags 'https://api.stackexchange.com/2.3/badges?tagged=python'
