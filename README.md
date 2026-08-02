# 📱 Paie Burkina Faso

[![Build APK](https://github.com/USERNAME/paie-burkina/actions/workflows/build.yml/badge.svg)](https://github.com/USERNAME/paie-burkina/actions/workflows/build.yml)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/)
[![KivyMD](https://img.shields.io/badge/KivyMD-1.1.1-green.svg)](https://kivymd.readthedocs.io/)

Application Android de gestion de paie conforme à la législation burkinabè (IUTS, CNSS, TPA).

## 🚀 Compilation automatique via GitHub Actions

### 1. Créer le repo GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/VOTRE_USER/paie-burkina.git
git push -u origin main
```

### 2. Lancer la compilation

Rendez-vous sur **Actions → Build Paie Burkina APK → Run workflow**.

La compilation dure environ **20 à 40 minutes** la première fois (téléchargement du SDK Android et des dépendances). Les builds suivants sont accélérés grâce au cache.

### 3. Récupérer l'APK

Une fois le workflow terminé, téléchargez l'APK dans l'onglet **Artifacts** de la page du workflow, ou directement depuis la section **Releases** si vous avez poussé un tag.

```bash
git tag v1.0.0
git push origin v1.0.0
```

Le tag déclenche automatiquement la création d'une Release GitHub avec l'APK attaché.

---

## 📋 Fonctionnalités

| Écran | Description |
|-------|-------------|
| **Settings** | Paramètres centralisés : taux CNSS, tranches IUTS, plafonds d'exonération |
| **Data Entry** | Saisie des employés (50 max) — Nom, Base, Prim, HS, Sursal, Gratif, Indemnités, Charges, Prêt |
| **Payroll Data** | Calculs automatiques : Rém Total, CNSS, IUTS progressif, Net Perçu, Charges patronales (TPA 3% + CNSS 16%) |
| **Journal Entries** | Écritures comptables SYSCOHADA prêtes à l'export |
| **Export Excel** | Génération d'un fichier `.xlsx` complet avec les 4 feuilles |

---

## 🧮 Calculs implémentés

| Élément | Formule | Valeur par défaut |
|---------|---------|-------------------|
| CNSS Employé | 5.5% de la Rém. Totale | Plafond 800 000 FCFA → max 44 000 |
| Plafond fiscal | 8% × (Sal + Prim + HS + Sursal) | — |
| Abattement | 20% CADRE / 25% AUTRE | — |
| Exonérations indemnités | Logement, Fonction, Transport | Plafonds paramétrables |
| IUTS | Progressif par tranches (12.1% → 25%) | 9 tranches |
| Réduction IUTS | Selon nombre de charges | 0→100%, 1→92%, 2→90%, 3→88%, 4+→86% |
| TPA | 3% de la Rém. Totale | — |
| CNSS Patronale | 16% de la Rém. Totale | — |
| Retenue obligatoire | 1% du Salaire Net | — |

---

## 📁 Structure du repo

```
.
├── .github/
│   └── workflows/
│       └── build.yml          # Workflow CI/CD GitHub Actions
├── main.py                     # Application KivyMD complète
├── buildozer.spec              # Configuration Buildozer
├── requirements.txt            # Dépendances Python
├── .gitignore
└── README.md                   # Ce fichier
```

---

## 🏗️ Compilation locale (alternative)

Si vous préférez compiler sur votre machine :

```bash
# Linux / WSL2
pip install buildozer cython
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

buildozer android debug
```

L'APK se trouve dans `./bin/`.

---

## 📊 Comptes SYSCOHADA

| Poste | Compte |
|-------|--------|
| Sal de Base | 661100 |
| Primes & Gratifications | 661200 |
| Heures Sup & Sursalaire | 661800 |
| Indemnité Caisse | 663800 |
| Indemnité Logement | 663100 |
| Indemnité Fonction | 663200 |
| Indemnité Transport | 663400 |
| Salaire Net | 422000 |
| Rosalaire | 447220 |
| Retenue Avance | 421000 |
| CNSS Employé | 431300 |
| IUTS | 447210 |
| CNSS Patronale | 664100 |
| TPA | 664200 |

---

## 📝 Licence

Propriétaire — VOTRE SOCIETE
