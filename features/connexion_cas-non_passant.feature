Feature: 'Essayer de se connecter avec un username non valide'

    En tant qu'utilisateur bloqué, je ne peux pas me connecter sur la page d'accueil de saucedemo.

    Scenario: 'Un utilisateur bloqué tente de se connecte sur le site saucedemo'

        Given je suis sur la page de connexion du site saucedemo 'https://www.saucedemo.com/'
        When je saisis mon identifiant 'locked_out_user' et mon mot de passe 'secret_sauce'
        Then je ne suis pas connecté sur le site saucedemo et un message d'erreur s'affiche
    