from pytest_bdd import scenarios, given, when, then, parsers
from pages.common_page import CommonPage
from pages.connexion_page import Connexion

# Initialisation des variables d'environnement
username = (By.ID, 'user-name')
password = (By.ID,'password')
button = (By.ID,'login-button')
saisi_username = "standard_user"
saisi_password = "secret_sauce"

# Chargement du fichier .feature
scenarios("../features/connexion.feature")


@given(parsers.parse("je suis sur la page de connexion du site saucedemo \'{url}\'"))
def ouverture_nav(prep_page,browser):
    prep_page.ouverture_navigateur(url)
    
@when(parsers.parse("je saisis mon identifiant \'{username}\' et mon mot de passe \'{password}\'"))
def connexion(prep_page,browser, username, password, button):
   # Pour le username
   prep_page.renseigner_champs(username)
    # Pour le password
    prep_page.renseigner_champs(password)





    

@when(parsers.parse("je recherche le lien du jeu '{keyword}' dans les {research_area:d} premiers résultats de recherche"))
def search_query(browser, search):
    result = click_google_play_result(search, limit=10)
    assert result.is_correct_game_displayed(search), f"Le jeu '{search}' n'est pas affiché sur la page de résultats."
    return result
    

@then(parsers.parse("je suis sur la page de '{keyword}' sur Google Play"))
def verify_results(browser, search, research_area):
    pass 