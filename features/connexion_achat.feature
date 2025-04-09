Feature: Connexion et commande d'articles sur Saucedemo
 
    Scenario: 'Un utilisateur se connecte sur le site saucedemo'

        Given je suis sur la page de connexion du site saucedemo 'https://www.saucedemo.com/'
        When je saisis mon identifiant 'standard_user' et mon mot de passe 'secret_sauce'
        Then je suis connecte sur le site saucedemo
 
    Scenario: Trier les produits du plus cher au moins cher

        Given je suis connecté sur le site saucedemo
        When je trie la liste des produits du plus cher au moins cher
        Then les produits sont triés du plus cher au moins cher
 
    Scenario: Ajouter les deux premiers produits au panier

        Given je suis connecté sur le site saucedemo
        When j'ajoute les deux premiers produits au panier
        Then les deux premiers produits ont été ajoutés au panier
 
    Scenario: Aller au panier

        Given je suis connecté sur le site saucedemo
        When je vais au panier
        Then je suis dans le panier
 
    Scenario: Vérifier que j'ai bien deux produits dans le panier

        Given je suis dans le panier
        When je vérifie que j'ai bien deux produits dans le panier
        Then il y a bien deux produits dans le panier
 
  Scenario: Saisir les informations du client

        Given je suis dans le panier
        When je saisis mes informations : nom "John Doe" et adresse "123 Rue de Test, 75000 Paris"
        Then les informations client "John Doe" et "123 Rue de Test, 75000 Paris" ont été saisies
 
    Scenario: Finaliser la commande

        Given je suis dans le panier
        When je finalise la commande
        Then la commande a été finalisée
 
    Scenario: Vérifier que la commande s'est bien réalisée

        Given la commande a été finalisée
        When je vérifie que la commande a été réalisée avec succès
        Then la commande a été réalisée avec succès
 