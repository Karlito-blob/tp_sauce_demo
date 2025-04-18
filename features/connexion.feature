Feature: 'Se connecter du site saucedemo'

    En tant qu'utilisateur standard je peux me connecter  et deconnecter sur saucedemo

    Scenario: 'Un utilisateur se connecte sur le site saucedemo'

        Given je suis sur la page de connexion du site saucedemo 'https://www.saucedemo.com/'
        When je saisis mon identifiant 'standard_user' et mon mot de passe 'secret_sauce'
        Then je suis connecte sur le site saucedemo
    
    Scenario: 'Un utilisateur se deconnecte sur le site saucedemo'
    
        Given je suis connecté sur le site saucedemo
        When je clique sur le bouton de deconnexion présent dans le menu
        Then je suis deconnecte du site saucedemo