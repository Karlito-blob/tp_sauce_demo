from .common_page import CommonPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



class Connexion(CommonPage):
   
    def renseigner_champs (self,locateur, saisi):
        super().click_element(locateur) 
        super().saisi_input(locateur,saisi)
        
    def confirmer_champs (self, locateur):
        super().click_element(locateur)
        
        
        
