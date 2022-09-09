from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class BizonePage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://bi.zone/'
        super().__init__(web_driver, url)

    logo = WebElement(class_name='header__logo')

    about_btn = WebElement(css_selector='.sectionEqual__button > span:nth-child(1)')

    find_open = WebElement(class_name='hSearch__open')

    find_str = WebElement(class_name='hSearch__search')

    find_lst = WebElement(class_name='hsResult__results')

