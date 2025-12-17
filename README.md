# ♥️ High-Low Card Game - Python Console Edition

A fun, fast-paced card game played in your terminal! The goal is to guess whether the next card drawn from a shuffled deck will be higher or lower in value than the card currently on the table.

This project is excellent for practicing:
* **List Manipulation:** Shuffling, popping, and counting items in a list.
* **Dictionaries:** Mapping numerical data to human-readable labels.
* **Boolean Logic:** Using comparison operators to determine win/loss states.

---

## ✨ Features

* **Complete 52-Card Deck:** Simulates a full deck, shuffled randomly at the start.
* **Face Card Mapping:** Automatically converts values like `1` to "Ace" and `13` to "King".
* **Score Tracking:** Keeps track of your consecutive correct guesses.
* **Tie Handling:** Recognizes when cards have the same value and doesn't penalize the player.

---

## 🚀 How to Run the Game

### 1. Prerequisites

You need **Python 3** installed on your computer. No third-party libraries are required.

### 2. Setup and Execution

1.  **Save the Code:** Save the Python code into a file named `card.py`.
2.  **Open Terminal:** Open your command prompt or terminal.
3.  **Run the Script:** Navigate to the file location and execute:

    ```bash
    python card.py
    ```

### 3. Gameplay Instructions

1.  The game reveals a "Starting Card."
2.  **Make a Guess:** Type `H` for Higher, `L` for Lower, or `Q` to Quit.
3.  **Results:** If you are right, your score increases and the new card becomes the reference for the next round.
4.  **Game Over:** One wrong guess ends the game! Try to see how long a streak you can get.

---

## 🧠 Core Python Concepts (Code Breakdown)

### 1. Simulating the Deck
We create a deck by repeating a range of numbers 4 times (for the four suits) and then use the `random` library to shuffle them.

```python
deck_values = list(range(1, 14)) * 4
random.shuffle(deck_values)

