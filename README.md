# MLOPS Computer vision

Ce projet est un exemple de mlops appliqué à des problematiques de computer vision.

## Introduction

Parmi les nombreux domaines de l'intelligence artificielle, aux côtés du traitement automatique du langage naturel, la vision par ordinateur (Computer Vision) a l'un des plus grands potentiels pour des applications pratiques. Compte tenu du volume important des images et vidéos générées sur le Web ou au sein des entreprises privées et des développements récents dans le domaine de l'apprentissage profond, les applications de Computer Vision (classification des images, détection d'objets, reconnaissance faciale, détection de scènes etc.) sont de plus en plus utilisées. À partir de 2012, nous avons assisté à un développement accéléré des algorithmes d'apprentissage profond pour la vision par ordinateur, avec des performances accrues sur diverses tâches année après année. Au cours de la même période, les frameworks d'apprentissage profond ont atteint une maturité qui leur permet d'être utilisés en dehors de la recherche, sur de nombreuses applications réelles. Toutefois, dans la pratique, il reste de nombreux défis à relever afin de mettre en œuvre efficacement les modèles de computer vision dans un scénario de production.

### Pré-requis

Ce qu'il est requis pour commencer:

- Docker
- set la variable d'environnement ${OUTPUT} qui se trouve dans le ``.env``
  - OUTPUT est le path de sortie des prédictions.
> Cette variables est utilisée pour monter en volume les dossiers dans notre Docker

### Installation

Pour lancer la création de l'image et la lancer à l'aide du docker-compose :  

``docker-compose up --build``

> Il est possible de rajouter ``-d`` pour détacher du terminal nos images.

Pour vérifier que l'image est bien lancée:  ``docker ps``.  

Vous devriez voir un container lancé.

Cependant il est possible de la construire et la lancer sans docker-compose.

``docker build -t <NAME> . ``

``docker run -p 5001:5001  --mount type=bind,source=$(OUTPUT),target=/app/result <NAME>``


> Il est possible de changer le port d'accès sur la machine `-p <PORT>:5001`, on peut aussi le modifier dans le `docker-compose.yml`.

## Utilisation

Une fois notre API lancé. Nous pouvons lui envoyer des requêtes.

Les requêtes doivent être envoyé sur le port 5001 (mais ce port peut-être modifié).

voici un exemple de requête en Python.



## Framework

- Mlflow
- DVC
- Fastapi
- Prometheus
- Grafana

## Installation

