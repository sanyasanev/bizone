import pytest
from pages.saucedemo import SaucePage

@pytest.mark.parametrize('test_name, username, passwd, expected_result',
                         [('Correctly login/pass for user "standard_user"', 'standard_user', 'secret_sauce', 'Products'),
                          ('Correctly login/pass for user "locked_out_user"', 'locked_out_user', 'secret_sauce', 'Products'),
                          ('Correctly login/pass for user "problem_user"', 'problem_user', 'secret_sauce', 'Products'),
                          ('Correctly login/pass for user "performance_glitch_user"',
                           'performance_glitch_user', 'secret_sauce', 'Products')])
def test_login(web_browser, test_name, username, passwd, expected_result):

    f"""
    {test_name}
    """

    souce_page_login = SaucePage(web_browser)

    souce_page_login.username_field.send_keys(username)

    souce_page_login.passwd_field.send_keys(passwd)

    souce_page_login.submit_btn.click()

    print(souce_page_login.title_on_page())

    assert souce_page_login.title_on_page() == expected_result
