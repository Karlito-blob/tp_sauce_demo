# IMPORTATION LIBRAIRIES :

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# CLASSE COMMUNE A TOUTE PAGE :

class CommonPage:

    # Définit le constructeur avec les attributs
    def __init__(self, browser):
        self.browser = browser

    # Ouverture du site
    def ouverture_navigateur(self, url):
        self.browser.get(url)
        self.browser.maximize_window()
        
    # Click sur un élément du site
    def click_element(self, locateur):
        element = WebDriverWait(self.browser, 10)
        element_trouve = element.until(EC.element_to_be_clickable(locateur))
        element_trouve.click()
        
    # Saisi d'une valeur dans une barre de recherche
    def saisi_input(self, locateur, saisi):
        element = WebDriverWait(self.browser, 10)
        element_saisi = element.until(EC.element_to_be_clickable(locateur))
        element_saisi.clear()
        element_saisi.send_keys(saisi)

    # Déterminer si l'élément est visible
    def element_visible(self, locateur):
        element = WebDriverWait(self.browser, 10)
        element_visible = element.until(EC.visibility_of_element_located(locateur))
        return element_visible
    
    # Trouver l'élément qui se trouve dans la page
    def element_present(self, locateur):
        element_present = self.browser.find_elements(*locateur)
        return element_present
    
        # * permet de decomposer l'element locateur (verifier de quel type il est et s'il se decompose bien en 2 elements)
        #return self.browser.find_elements(locateur[0],locateur[1])