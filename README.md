# modern-devops-platform

Projet fil rouge pour apprendre le DevOps moderne de façon progressive, pratique et documentée.

## Objectifs

Construire une plateforme complète en plusieurs blocs :

- API backend
- Base de données PostgreSQL
- Cache Redis
- Docker
- Docker Compose
- Monitoring avec Prometheus et Grafana
- Tests et qualité
- CI/CD avec GitHub Actions
- Kubernetes
- Terraform
- Déploiement cloud

## Méthode d'apprentissage

Chaque bloc suit la même logique :

1. comprendre le rôle du bloc
2. comprendre la structure des fichiers
3. lire le code
4. expliquer le code
5. écrire le code soi-même
6. tester
7. documenter les erreurs et solutions

## Structure du projet

- `docs/` : notes d'apprentissage, architecture, liens vers documentation officielle
- `logs/` : erreurs rencontrées, correctifs, checklists de debug
- `app/` : application backend
- `docker/` : conteneurisation et orchestration locale
- `monitoring/` : Prometheus, Grafana, métriques
- `ci/` : documentation CI/CD
- `k8s/` : manifests Kubernetes
- `terraform/` : infrastructure as code

## Ordre recommandé des blocs

1. Fondations
2. API backend
3. PostgreSQL
4. Redis
5. Docker
6. Docker Compose
7. Monitoring
8. Tests et qualité
9. GitHub Actions
10. Sécurité
11. Kubernetes
12. Terraform
13. Cloud

## Règle de travail

Ne jamais passer au bloc suivant sans comprendre le précédent.