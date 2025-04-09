from pytest_bdd import scenarios, given, when, then, parsers
from pages.connexion_page import Connexion
from pages.home_page import HomePage
from selenium.webdriver.common.by import By

# Initialisation des variables d'environnement
username = (By.ID, 'user-name')
password = (By.ID,'password')
button = (By.ID,'login-button')
saisi_username = "locked_out_user"
saisi_password = "secret_sauce"
message_error = (By.XPATH, '//h3[text() = "Epic sadface: Sorry, this user has been locked out."]')


# Chargement du fichier .feature
scenarios("../features/connexion_cas-non_passant.feature")

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

@then("je ne suis pas connecté sur le site saucedemo et un message d'erreur s'affiche")
def erreur_connecte(prep_page):
    assert prep.page.element_visible(message_error) # Élément indiquant la connexion est bloquée"
    print("Un message d'erreur s'affiche : Epic sadface: Sorry, this user has been locked out.")
