import requests

from pytest_bdd import scenarios, given, then, parsers

DUCKDUCKGO_API = 'https://api.duckduckgo.com/'

EXTRA_TYPES = {'String': str}

scenarios('../features/service.feature')


@given(parsers.cfparse('the DuckDuckGo API is queried with "{phrase:String}"', extra_types=EXTRA_TYPES),
       target_fixture='response')
def ddg_response(phrase):
    params = {'q': phrase, 'format': 'json'}
    response = requests.get(DUCKDUCKGO_API, params=params)
    return response


@then(parsers.cfparse('the response contains results for "{phrase:String}"', extra_types=EXTRA_TYPES))
def ddg_response_contents(response, phrase):
    assert phrase.lower() == response.json()['Heading'].lower()


@then(parsers.parse('the response status code is "{code:d}"'))
def ddg_response_code(response, code):
    print("asserting response")
    assert response.status_code == code
