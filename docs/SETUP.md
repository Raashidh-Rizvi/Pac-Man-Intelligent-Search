# Environment Setup & Verification Guide — SE3062 Pac-Man Project

This document provides complete instructions for setting up, configuring, and verifying the development environment for the **SE3062 — Intelligent Systems: Pac-Man Intelligent Search** project.

---

## 1. System Requirements

The project runtime and development environment require the following components:

- **Python:** 3.9 – 3.11 (Python 3.11 recommended)
- **Package Manager:** Conda or standard `pip` / `venv`
- **Numerical & Plotting Packages:**
  - `numpy` (for matrix operations & state calculations)
  - `matplotlib` (for heuristic visualization & performance plotting)
- **Version Control:** Git (required for version control and group collaboration)

---

## 2. Recommended Conda Setup (Windows PowerShell)

For users using Anaconda or Miniconda:

```powershell
# 1. Create a clean Conda environment with Python 3.11
conda create -n se3062-pacman python=3.11 -y

# 2. Activate the environment
conda activate se3062-pacman

# 3. Install required third-party dependencies
pip install -r requirements.txt
```

---

## 3. Alternative Standard Pip / Venv Setup (Windows PowerShell)

For users using standard Python without Conda:

```powershell
# 1. Create a virtual environment named .venv in the project root
python -m venv .venv

# 2. Activate the virtual environment in PowerShell
.venv\Scripts\Activate.ps1

# 3. Install required third-party dependencies
pip install -r requirements.txt
```

> **Linux/macOS Option (Bash):**
> ```bash
> python3 -m venv .venv
> source .venv/bin/activate
> pip install -r requirements.txt
> ```

---

## 4. Environment Verification Commands

Verify that the environment has been installed correctly by executing the following commands in PowerShell:

```powershell
# Check Python version (should report Python 3.9.x - 3.11.x)
python --version

# Check pip version
pip --version

# Verify NumPy installation
python -c "import numpy; print('NumPy:', numpy.__version__)"

# Verify Matplotlib installation
python -c "import matplotlib; print('Matplotlib:', matplotlib.__version__)"
```

### Expected Verification Output
- `python --version` outputs Python version within range `3.9` to `3.11` (e.g., `Python 3.11.9`).
- `pip --version` displays the active virtual environment path.
- `NumPy` and `Matplotlib` commands print installed version numbers without `ImportError` or warnings.

---

## 5. Running the Application

All execution commands must be run from the repository root directory containing the core assignment files:

```text
pacman.py
search.py
searchAgents.py
util.py
autograder.py
```

### Launch Pac-Man Game

To start the interactive GUI application:

```powershell
python pacman.py
```

### Expected Behavior
- Pac-Man graphical interface (Tkinter window) opens.
- The default maze layout renders correctly.
- Player can control Pac-Man using standard Keyboard Arrow keys (`Up`, `Down`, `Left`, `Right`).

---

## 6. Running Assignment Autograder Tests

The project includes an automated grading tool (`autograder.py`) to test search algorithm implementations.

### Individual Question Verification (Development Mode)

Run specific test suites during algorithm development:

```powershell
# Q1 — Depth First Search
python autograder.py -q q1

# Q2 — Breadth First Search
python autograder.py -q q2

# Q3 — Uniform Cost Search
python autograder.py -q q3

# Q4 — A* Search
python autograder.py -q q4

# Q5 — CornersProblem State Representation
python autograder.py -q q5

# Q6 — Corners Heuristic
python autograder.py -q q6

# Q7 — Food Heuristic
python autograder.py -q q7
```

### Full Autograder Regression Test

Before submitting or pushing changes to `main`, execute the full test suite:

```powershell
python autograder.py
```

### Usage Explanation
- **Individual Question Commands (`-q qN`):** Fast, targeted testing during active development of a specific question.
- **Full Autograder Command (`python autograder.py`):** Used for complete regression testing to ensure no previously passed tests broke during refactoring.

---

## 7. Troubleshooting

- **Powershell Execution Policy Error on `Activate.ps1`:**
  Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` in PowerShell to enable local script execution.
- **Missing Tkinter Window:**
  Ensure Python standard library includes `tkinter` support (standard on Windows Python installers).
