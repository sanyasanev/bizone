from pages.base import WebPage
from pages.elements import WebElement


class SaucePage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://www.saucedemo.com/'
        super().__init__(web_driver, url)

    username_field = WebElement(id='user-name')

    passwd_field = WebElement(name='password')

    submit_btn = WebElement(css_selector='[data-test="login-button"]')

    title_on_page = WebElement(css_selector='[title="Products"]')

