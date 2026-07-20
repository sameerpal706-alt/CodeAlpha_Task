# CodeAlpha_Task
# 🎮 Hangman Game (Python)

A simple command-line Hangman game built using Python. The program randomly selects a word from a predefined list, and the player must guess the word one letter at a time before running out of attempts.

## 📌 Features

- Random word selection
- 5 predefined words
- 6 incorrect guesses allowed
- Prevents repeated letter guesses
- Displays the word progress after each guess
- Win and lose messages

## 🛠️ Requirements

- Python 3.x

No external libraries are required. The game only uses Python's built-in `random` module.

## ▶️ How to Run

1. Save the Python code in a file named `hangman.py`.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the following command:

```bash
python hangman.py
```

## 🎯 How to Play

1. The game randomly selects a word.
2. The word is displayed as underscores (`_`).
3. Enter one letter at a time.
4. If the letter exists in the word, it is revealed.
5. If the letter is incorrect, one attempt is deducted.
6. The game ends when:
   - You guess the entire word, or
   - You run out of attempts.

## 📂 Project Structure

```
Hangman-Game/
│── hangman.py
└── README.md
```

## 📸 Sample Output

```
Welcome to Hangman Game!
You have 6 incorrect guesses.

Word: _ _ _ _ _

Enter a letter: p
Correct!

Word: p _ _ _ _ _

Enter a letter: z
Wrong guess!
Remaining attempts: 5
```

## 🚀 Future Improvements

- Input validation
- Hangman ASCII art
- Play again option
- Difficulty levels
- Larger word list
- Score tracking

## 📚 Concepts Used

- Python Lists
- Loops (`while`, `for`)
- Conditional Statements (`if`, `else`)
- User Input
- String Manipulation
- Random Module

## 👨‍💻 Author

Developed as a beginner-friendly Python project to practice programming fundamentals.

## 📄 License

This project is open source and available under the MIT License.
