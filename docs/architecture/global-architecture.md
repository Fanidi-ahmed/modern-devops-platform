# Architecture globale

## Vision

Le projet modern-devops-platform est une plateforme d'apprentissage DevOps moderne construite bloc par bloc.

## Composants prévus

- API backend
- PostgreSQL
- Redis
- Prometheus
- Grafana
- Docker
- Docker Compose
- GitHub Actions
- Kubernetes
- Terraform

## Flux simplifié

Client -> API -> PostgreSQL
Client -> API -> Redis
Prometheus -> scrape metrics API
Grafana -> visualisation des métriques Prometheus

## Objectif pédagogique

Comprendre profondément :
- le rôle de chaque composant
- les échanges réseau
- la persistance
- l'observabilité
- l'automatisation
- le déploiement

## Principe

Construire petit, comprendre profondément, documenter systématiquement.