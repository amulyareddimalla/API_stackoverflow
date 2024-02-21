from urllib.parse import urlparse, parse_qs

import requests

# Function to generate authorization code
def generate_code():
    # Make a request to StackExchange API to get the access token
    response = requests.post('https://stackoverflow.com/oauth', data={
        'client_id': '28323',
        'scope': 'no_expiry',
        'redirect_uri': 'https://stackexchange.com/oauth/login_success'
    })
    # Extract and return the authorization code from the redirect URL
    redirect_url = response.url
    parsed_url = urlparse(redirect_url)
    query_params = parse_qs(parsed_url.query)
    authorization_code = query_params.get('code')
    if authorization_code is None:
        print("Error: Authorization code not found in redirect URL")
    else:
        authorization_code = authorization_code[0]
        print("Authorization Code:", authorization_code)

    return authorization_code

# Function to generate StackExchange API token
def generate_api_token(authorization_code):
    # Make a request to StackExchange API to get the access token
    response = requests.post('https://stackoverflow.com/oauth/access_token', data={
        'client_id': '28323',
        'client_secret': 'M*XpFDDKJ5Z)7EvnDY2fUA((',
        'code': authorization_code,
        'redirect_uri': 'https://stackexchange.com/oauth/login_success'
    })
    # Check if the response was successful
    if response.status_code == 200:
        # Parse the response content
        response_data = parse_qs(response.text)
        # Extract and return the access token
        return response_data.get('access_token', [''])[0]
    else:
        # If the request was not successful, raise an error
        response.raise_for_status()

# Generate authorization code
authorization_code = generate_code()

# Generate StackExchange API token using the authorization code
access_token = generate_api_token(authorization_code)
print("Access Token:", access_token)

# Function to perform API level tests for StackExchange badges API
def test_badges_api(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    # Test case for fetching badges by ids
    response = requests.get('https://api.stackexchange.com/2.3/badges/1;2', headers=headers)
    assert response.status_code == 200, "Failed to fetch badges by ids"

    # Test case for fetching badges by recipients
    response = requests.get('https://api.stackexchange.com/2.3/badges?recipients=12345', headers=headers)
    assert response.status_code == 200, "Failed to fetch badges by recipients"

    # Test case for fetching badges by tags
    response = requests.get('https://api.stackexchange.com/2.3/badges?tagged=python', headers=headers)
    assert response.status_code == 200, "Failed to fetch badges by tags"

    print("All API tests passed successfully")

def test_api():
    #To generate Code
    generate_code()

    #To generate Access Token
    generate_api_token(authorization_code)

    # Perform API level tests for StackExchange badges API
    test_badges_api(access_token)


# Run the main function
test_api()
