# CI/CD – Déploiement automatique d'une application Flask
1. Présentation

Ce projet consiste à mettre en place une chaîne CI/CD permettant de tester, construire et déployer automatiquement une application web Flask.

L'application expose deux endpoints :

• `/health` : vérification de l'état de l'application

• `/addition` : endpoint de test

L'application écoute sur le port `8080` dans le conteneur Docker.

2. Fonctionnement du pipeline

Le pipeline GitHub Actions est déclenché automatiquement à chaque `push` sur la branche `main`.

Il comporte les étapes suivantes :

1. Exécution des tests unitaires avec `unittest`.

2. Exécution des tests E2E avec `pytest`.

3. Construction de l'image Docker.

4. Publication de l'image sur Docker Hub.

5. Connexion à la VM du professeur via SSH.

6. Déploiement de la nouvelle image Docker.

7. Vérification de l'application avec l'endpoint `/health`.

Les étapes de build et de déploiement sont exécutées uniquement si les tests précédents réussissent.

3. Déclenchement du déploiement

Le déploiement est entièrement automatique.

Un simple :

`git push origin main`

déclenche le workflow GitHub Actions.

GitHub Actions se charge ensuite automatiquement du déploiement sur la VM. Aucune commande de déploiement n'est exécutée manuellement sur la VM.

4. Choix techniques

• **Flask** : framework Python léger pour développer l'application web.

• **Docker** : conteneurisation de l'application afin d'avoir un environnement de déploiement reproductible.

• **Docker Hub** : stockage et distribution de l'image Docker.

• **GitHub Actions** : automatisation des tests, du build et du déploiement.

• **SSH** : connexion sécurisée entre GitHub Actions et la VM.

• **GitHub Secrets** : stockage des informations sensibles utilisées par le pipeline.

Le conteneur utilise le port `8080` et est exposé sur le port `8094` de la VM.

L'application est accessible via l'IP publique de la VM sur le port `8094`.

Exemple : `http://<IP_PUBLIQUE_VM>:8094/health`

5. Application déployée

L'application déployée peut être vérifiée avec l'endpoint `/health`. Celui-ci retourne le statut de l'application.

Une capture d'écran de l'application accessible depuis l'IP publique de la VM peut être ajoutée au dépôt dans le dossier `screenshots/`.

Structure du dépôt

app.py

requirements.txt

Dockerfile

README.md

tests/test_app.py

e2e/test_e2e.py

.github/workflows/ci-cd.yml

screenshots/application-vm.png
