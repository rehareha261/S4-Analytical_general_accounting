# S4_ERP Project

S4_ERP est un projet basé sur Django, conçu pour gérer différents aspects des opérations ERP (Enterprise Resource Planning). Ce document décrit les principales fonctionnalités du projet.

## Fonctionnalités Principales

1. **Configuration ASGI et WSGI**:
    - `asgi.py` et `wsgi.py` configurent respectivement les serveurs ASGI et WSGI pour le projet. Ils exposent des appels de modules pour une utilisation lors du déploiement.
    
2. **Gestionnaire de Tâches Administratives**:
    - `manage.py` est l'utilitaire en ligne de commande de Django pour les tâches administratives telles que les migrations de base de données, le lancement du serveur de développement, etc.

3. **Paramètres du Projet**:
    - `settings.py` contient les paramètres de configuration du projet, y compris la configuration des applications installées, les middlewares, la base de données, etc.

4. **Application Comptable**:
    - `comptable.apps.py` est la configuration de l'application comptable, qui gère divers aspects de la comptabilité.
    - `comptable.admin.py` configure l'interface d'administration pour les modèles comptables.
    - `comptable.templatetags.filters.py` implémente des filtres définis par l'utilisateur pour des manipulations de données spécifiques dans les templates.
    
5. **Migrations**:
    - `0002_alter_historiquesociete_logo_and_more.py` est un fichier de migration qui effectue des modifications de schéma dans la base de données, tels que l'altération des champs existants.

6. **Fichiers de Configuration Web**:
    - `urls.py` contient les mappings URL du projet, assurant la redirection correcte des requêtes vers les vues appropriées.

7. **Dépendances**:
    - `requirements.txt` spécifie les packages Python nécessaires pour exécuter le projet.

## Conventions de Code

- **Nommage**: Les fonctions utilisent le style `snake_case` et les classes `PascalCase`.
- **Imports Courants**: Importations de modules standards tels que `os`, `pathlib`, ainsi que des modules spécifiques comme `comptable` et `S4_ERP`.

## Déploiement

Pour plus d'informations sur le déploiement et d'autres configurations avancées, consultez la documentation officielle de Django [ici](https://docs.djangoproject.com/en/stable/).

---