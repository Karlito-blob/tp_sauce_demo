from pytest_bdd import scenarios, given, when, then, parsers
from pages.common_page import CommonPage
from pages.connexion_page import Connexion
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialisation des variables d'environnement
username = (By.ID, 'user-name')
password = (By.ID,'password')
button = (By.ID,'login-button')
saisi_username = "standard_user"
saisi_password = "secret_sauce"
home_page = (By.ID, 'inventory_container')

# Chargement du fichier .feature
scenarios("../features/connexion.feature")

@given(parsers.parse("je suis sur la page de connexion du site saucedemo \'{url}\'"))
def ouverture_nav(prep_page,browser, url):
    prep_page.ouverture_navigateur(url)
    
@when(parsers.parse("je saisis mon identifiant '{saisi_username}' et mon mot de passe '{saisi_password}'"))

def connexion(prep_page, saisi_username, saisi_password):
    prep_page.__class__ = Connexion
    prep_page.renseigner_champs(username, saisi_username)
    prep_page.renseigner_champs(password, saisi_password)
    prep_page.confirmer_champs(button)

@then("je suis connecte sur le site saucedemo")
def connecte(prep_page):
    prep_page.__class__ = HomePage
    assert prep_page.element_present(home_page), "Élément indiquant la connexion non trouvé"
    print("je suis bien connecté")