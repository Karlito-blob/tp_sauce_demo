from pytest_bdd import scenarios, given, when, then, parsers
from pages.connexion_page import Connexion
from pages.home_page import HomePage
from selenium.webdriver.common.by import By

# Initialisation des variables d'environnement
username = (By.ID, 'user-name')
password = (By.ID,'password')
button = (By.ID,'login-button')
saisi_username = "standard_user"
saisi_password = "secret_sauce"
home_page = (By.ID, 'inventory_container')

menu_burger = (By.ID, 'react-burger-menu-btn')
logout_button = (By.ID, 'logout_sidebar_link')

# Chargement du fichier .feature
scenarios("../features/connexion.feature")

# Scénario 1 : connexion avec un utilisateur standard
@given(parsers.parse("je suis sur la page de connexion du site saucedemo \'{url}\'"))
def ouverture_nav(prep_page, url):
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
    
# scénario 2 : déconnexion avec un utilisateu-r standard
@given(parsers.parse("je suis connecté sur le site saucedemo"))
def connected(prep_page):
    ouverture_nav(prep_page, "https://www.saucedemo.com/")
    connexion(prep_page, saisi_username, saisi_password)
    connecte(prep_page)
    print("je suis bien connecté")

@when(parsers.parse("je clique sur le bouton de deconnexion présent dans le menu"))
def click_menu_burger(prep_page):
    prep_page.deconnexion(menu_burger, logout_button)
    
@then("je suis deconnecte du site saucedemo")
def deconnecte(prep_page):
    assert prep_page.element_present(button), "Élément indiquant la déconnexion non trouvé"
    print("je suis bien déconnecté")