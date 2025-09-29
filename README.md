# Parking Optimization Project
**Optimization of multi-level automated parking systems using heuristic algorithms (A* search and simulated annealing).**

## Overview
This repository contains the source code of the **Parking Optimization Project**.
The objective is to model and optimize vehicle placement in automated multi-level parking systems, in order to minimize the **retrieval cost** (number of moves required to extract a car).

## Author
- Maxence DEBES

## Repository structure
- `scripts/` : Python scripts implementing the parking model and optimization algorithms.
- `results/` : outputs from experiments (logs, plots, benchmarks).
- `docs/` : reports and presentations related to the project.

## Details of directories and scripts

- **`scripts/`**
  Contains the Python code of the project.
  - `algorithme_A_etoile.py` → A* search algorithm implementation.
  - `recuit_simule.py` → simulated annealing optimization.
  - `heuristique.py` → heuristic function used by A*.
  - `cout.py`, `cout_actuel.py`, `cout_moyen.py` → cost computations.
  - `creer_parking.py` → parking grid creation.
  - `enfants_noeud.py` → generation of successor states.
  - `generer_aleatoire.py` → generate random parking instances.
  - `generer_voisin_aleatoire.py` → generate random neighbors (for simulated annealing).
  - `dessiner_parking.py` → visualization of parking layouts using pygame.

- **`docs/`**
  Contains additional documents.
  - `TIPE - Présentation finale.pdf` → final presentation (PDF).
  - `TIPE – Présentation finale.pptx` → final presentation (PowerPoint).

## Installation
```bash
git clone https://github.com/maxencedbe/parking-optimization.git
cd parking-optimization
pip install -r requirements.txt  

Dependencies:
- `numpy`
- `pygame`
```

## License
Developed by Maxence DEBES.

Distributed under the **MIT license**.