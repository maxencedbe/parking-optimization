# Automated Parking Optimization

This project models and optimizes **multi-level automated parking systems** using heuristic algorithms (A* search and simulated annealing). The objective is to minimize the **vehicle retrieval cost** in puzzle-like automated parking layouts.

---

## Repository Structure
parking-optimization/
│ README.md
│ requirements.txt
│
├───scripts/
│ algorithme_A_etoile.py # A* search implementation
│ recuit_simule.py # Simulated annealing
│ heuristique.py # Heuristic function
│ cout.py # Cost computation
│ cout_actuel.py # Current cost calculation
│ cout_moyen.py # Average cost calculation
│ creer_parking.py # Build a parking grid
│ enfants_noeud.py # Generate successor states
│ generer_aleatoire.py # Generate random parking
│ generer_voisin_aleatoire.py # Generate random neighbor
│ dessiner_parking.py # Visualize parking with pygame
│ run_experiments.py # Main entry point

---

## Installation
```bash
git clone https://github.com/<username>/parking-optimization.git
cd parking-optimization
pip install -r requirements.txt