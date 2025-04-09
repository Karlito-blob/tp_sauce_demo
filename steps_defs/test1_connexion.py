from pytest_bdd import scenarios, given, when, then, parsers
from pages.common_page import CommonPage
from pages.connexion_page import Connexion
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialisation des variables d'environnement
username = (By.ID, 'user-name')
password = (By.ID,'password')
button = (By.ID,'login-button')
saisi_username = "standard_user"
saisi_password = "secret_sauce"
home_page = (By.ID, 'inventory container')

# Chargement du fichier .feature
scenarios("../features/connexion.feature")


@given(parsers.parse("je suis sur la page de connexion du site saucedemo \'{url}\'"))
def ouverture_nav(prep_page,browser):
    prep_page.ouverture_navigateur(url)
    
@when(parsers.parse("je saisis mon identifiant \'{saisi_username}\' et mon mot de passe \'{saisi_password}\'"))
def connexion(prep_page, browser, username, saisi_username, password, saisi_password, button):
    # Pour le username
    prep_page.__class__ = Connexion
    prep_page.renseigner_champs(username, saisi_username)
    # Pour le password
    prep_page.renseigner_champs(password, saisi_password)
    prep_page.confirmer_champs(button)
    
@then("je suis connecte sur le site saucedemo")
def connecte(prep_page, browser,home_page)
    prep_page.__class__ = HomePage
    prep_page.element_present(home_page)
    print("je suis bien connecte")
    






    


    

@then(parsers.parse("je suis sur la page de '{keyword}' sur Google Play"))
def verify_results(browser, search, research_area):
    pass 