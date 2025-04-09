from .common_page import CommonPage
import time


class HomePage(CommonPage):
    
    def deconnexion(self, locateur1, locateur2):
        super().click_element(locateur1)
        time.sleep(2)
        super().click_element(locateur2)  
        
    def filtrer(self, locateur1, locateur2):  
        super().click_element(locateur1)
        time.sleep(2)
        super().click_element(locateur2)

    def obtenir_prix(self,locateur):
    # Trouver tous les éléments de prix sur la page via XPath
        prix_elements = super().element_visible(locateur)
    # Extraire les prix et les convertir en float (pour pouvoir les comparer)
        prix_list = [float(prix.text.replace('$', '').strip()) for prix in prix_elements]
        return prix_list