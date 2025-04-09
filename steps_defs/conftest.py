# IMPORTATION LIBRAIRIES
import pytest
from selenium import webdriver
from pages.common_page import CommonPage


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


# FIXTURES

# Fixture : Type de navigateur
@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()

# Fixture : Réutiliser la page
@pytest.fixture
def prep_page(browser):
    Page = CommonPage(browser)
    yield Page