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
bouton_filtre = (By.XPATH,'//select') 
trier_prix = (By.XPATH,'//option[@value = "hilo"]')
liste_prix = (By.XPATH, '//div[@class="inventory_item_price"]')

# Chargement du fichier .feature
scenarios("../features/connexion_achat.feature")

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
    
# Scénario 2: Trier les produits du plus cher au moins cher

@given("je suis connecté sur le site saucedemo")
def connected(prep_page):
    ouverture_nav(prep_page, "https://www.saucedemo.com/")
    connexion(prep_page, saisi_username, saisi_password)
    connecte(prep_page)
    print("je suis bien connecté")
    

@when("je trie la liste des produits du plus cher au moins cher")
def trier_par_prix(prep_page):
    # Vérification que les prix sont visibles avant d'appliquer le tri
    assert prep_page.element_visible(liste_prix), "Les prix ne sont pas visibles"
    # Récupérer les prix avant d'appliquer le tri
    prix_avant = obtenir_prix(prep_page)
    # Appliquer le filtre pour trier les produits par prix décroissant
    prep_page.filter(bouton_prix, trier_prix)  # bouton_prix et trier_prix sont des variables ou des sélecteurs définis
     # Vérification que les prix sont visibles après le tri
    assert prep_page.element_visible(liste_prix), "Les prix ne sont pas visibles après le tri"
    # Récupérer les prix après avoir appliqué le tri
    prix_apres = obtenir_prix(liste_prix)
    # Vérification que la liste des prix est triée correctement (du plus cher au moins cher)
    assert prix_apres == sorted(prix_apres, reverse=True), "Les prix ne sont pas triés du plus cher au moins cher"
    print("Les produits sont triés correctement du plus cher au moins cher.")
    
@then('les produits sont triés du plus cher au moins cher')
def affiche_produit_le_plus_cher(prep_page)
    assert prep_page.element_visible()

