import pytest
from pages.bizone_main import BizonePage

def test_availability(web_browser, element, expected_result):

    '''
    Наличие, видимость, кликабельность элементов на странице
    '''

    page = BizonePage(web_browser)

    page.logo.is_presented()

    page.logo.is_visible()

    page.logo.is_clickable()

    page.about_btn.is_presented()

    page.about_btn.is_visible()

    page.about_btn.is_clickable()

@pytest.mark.parametrize('search_text, expected_text',
                         [('кибербезопасности Cyber Polygon 2021', 'Как прошел международный онлайн-тренинг по кибербезопасности Cyber Polygon 2021'),
                          ('hkj', 'К сожалению, мы не смогли найти ничего по "hkj". Попробуйте переформулировать запрос.')])
def test_search(web_browser, search_text, expected_text):
    '''
    Строка поиска предлагает варианты
    '''

    page = BizonePage(web_browser)

    page.find_str.is_not_visible()

    page.find_open.click()

    page.find_str.click()

    page.find_str.send_keys(search_text)

    assert page.find_lst.get_text == expected_text

