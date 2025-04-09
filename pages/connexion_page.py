from .common_page import CommonPage


class Connexion(CommonPage):
   
    def renseigner_champs (self,locateur, saisi):
        super().click_element(locateur) 
        super().saisi_input(locateur,saisi)
        
    def confirmer_champs (self, locateur):
        super().click_element(locateur)