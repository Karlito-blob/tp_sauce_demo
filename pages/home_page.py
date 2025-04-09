from .common_page import CommonPage
import time


class HomePage(CommonPage):
    
    def deconnexion(self, locateur1, locateur2):
        super().click_element(locateur1)
        time.sleep(2)
        super().click_element(locateur2)     