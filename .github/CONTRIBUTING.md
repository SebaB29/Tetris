# Contributing to Tetris Game

Thank you for your interest in contributing! This project was developed as a university assignment, but any improvements, bug fixes, or new ideas are more than welcome to make this puzzle classic even better.

## How to Contribute

1. **Fork** the repository.
2. Create your branch: `git checkout -b feature/new-functionality`.
3. Make your changes and commit them: `git commit -m "Add new functionality"`.
4. Push your branch: `git push origin feature/new-functionality`.
5. Open a **Pull Request**.

## Ideas for Contribution

- **New Game Modes:** Implement "Sprint" (clear 40 lines), "Ultra" (score as much as possible in 3 minutes), or "Versus" mode.
- **Visual Improvements:** Add animations for line clears, ghost piece (shadow where the piece will land), or custom block skins.
- **Advanced Scoring:** Implement a "Combo" system or T-Spin detection for higher scores.
- **Enhanced Data Management:** Improve the SQLite implementation to include player profiles, dates, or online leaderboards.
- **Code Refactoring:** Decouple the GUI from the game logic or improve the piece rotation system (SRS - Super Rotation System).

## Development Tips

- **Database Safety:** If you modify the `sistema_puntaje.py`, ensure the database connection is handled safely to avoid corrupting the `.db` file.
- **Piece Configuration:** New Tetromino shapes can be added directly to `resources/piezas.txt`. Check the format before adding new ones.
- **Clean Logic:** Keep the grid manipulation inside `tablero.py` and the piece logic inside `pieza.py`.

Thank you for your collaboration! 🎉
