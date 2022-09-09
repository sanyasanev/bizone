import pytest
from requests_html import HTMLSession


@pytest.mark.parametrize('query_param, _url, expected_result',
                         [('28', 'ya.ru', 200),
                          ('werw', 'google.com', 404)])
def test_request(query_param, _url, expected_result):
    session = HTMLSession()
    r = session.post(f'https://{_url}...{query_param}...', verify=False,
                     headers={'Authorization': 'Basic {...}'})
    assert r.status_code == expected_result

