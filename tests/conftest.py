from selene.support.shared import browser
import pytest

@pytest.fixture(scope='function', autouse=True)
def form_management():
    yield
    browser.quit()