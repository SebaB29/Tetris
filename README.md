# 🎮 Tetris Game

Welcome to **Tetris**, a classic puzzle game implementation in Python. Arrange falling blocks (Tetrominoes) to clear lines, score points, and save your high scores in a local database. This project focuses on Object-Oriented Programming (OOP) and persistent data management.

# 📸 Demo
<div align="center">
    <img alt="Tetris Gameplay Demo" src="img/TetrisDemo.gif" width="400px">
</div>

# 📍 Table of Contents
- [📝 Description](#-description)
  - [🧩 Key Features](#-key-features)
  - [🧱 Project Structure](#-project-structure)
  - [🛠️ Technologies](#️-technologies)
- [🚀 Getting Started](#-getting-started)
  - [📋 Prerequisites](#-prerequisites)
  - [⚙️ Installation](#️-installation)
- [💡 Usage](#-usage)
- [🤝 Contributing](#-contributing)
- [👥 Team](#-team)
- [📄 License](#-license)

# 📝 Description
This project is a university assignment designed to master complex game logic and data persistence. It features a custom graphical interface and a backend system to manage player scores using SQLite.

## 🧩 Key Features
- **Classic Mechanics:** Line clearing, block rotation, and increasing difficulty.
- **Persistent Scoring:** High scores are saved locally using an SQLite3 database.
- **Customizable Pieces:** Tetromino shapes are loaded from an external configuration file (`piezas.txt`).
- **Game State Management:** Includes pause, game over, and real-time score tracking.

## 🧱 Project Structure
```text
Tetris/
├── graphics/    # UI rendering and Gamelib integration
├── img/         # Demo GIF and screenshots
├── resources/   # Piece definitions (piezas.txt)
├── src/         # Core logic
│   ├── tablero.py        # Grid logic
│   ├── pieza.py          # Tetromino behavior
│   ├── sistema_puntaje.py # SQL database management
│   └── tetris.py         # Main game engine
└── main.py      # Entry point
```

## 🛠️ Technologies
* **Python 3.x**
* **SQLite3**: For persistent score storage.
* **Gamelib**: A thread-based rendering library.

# 🚀 Getting Started
## 📋 Prerequisites
* Python 3.10 or higher.
* SQLite3 (usually bundled with Python).

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/SebaB29/Tetris.git](https://github.com/SebaB29/Tetris.git)
   cd Tetris
   ```
2. Ensure resources are present:
   Make sure resources/piezas.txt is in the directory before running.

# 💡 Usage
Launch the game by running:
```bash
python main.py
```

## 🎮 Controls
| Key         | Action         |
|-------------|----------------|
| Arrow Up    | Move Up        |
| Arrow Down  | Move Down      |
| Arrow Left  | Move Left      |
| Arrow Right | Move Right     |
| P           | Pause / Resume |

# 🤝 Contributing
1. Fork the project.
2. Create your Feature Branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to the Branch (git push origin feature/AmazingFeature).
5. Open a Pull Request.

# 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
