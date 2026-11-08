# ShadowLock - Secure Password Manager Vault 🔐🔑

ShadowLock is a secure, object-oriented console application built in Python to safely store and manage digital account credentials. It implements strict validation checkpoints, including an initial Master Password authorization gate, a real-time password complexity evaluator, and custom file writing mechanisms to preserve user states across runs.

---

## 🌟 About the Developer

*   **Age/Class:** 16 Years Old (Class 10th) 🎯
*   **Future Goal:** B.Tech in Artificial Intelligence and Machine Learning (AI-ML).
*   **Milestone:** Successfully completed the **100 Days of Code** challenge!
*   **Current Focus:** Learning Data Structures & Algorithms (DSA) and data science libraries like **NumPy** and **Pandas**.

---

## ✨ Key Features

*   **Master Security Gate:** Blocks all core menu tracking paths until the user passes validation against a secure master password key (`krishna`).
*   **Complexity Evaluator:** Automatically scans newly added passwords against strict strength rules (minimum 8 characters, at least 1 digit, and 1 special symbol), issuing weak warning alerts before adding data.
*   **Conditional Masked Previews:** Provides granular lookups where users can either selectively reveal cleartext strings or securely display masked elements (`********`).
*   **Scratch-Built Data Exporters:** Implements native system data writing without importing serialization libraries:
    *   **Custom CSV Parser:** Manually structures string matrices with trailing header fields (`.csv`).
    *   **Manual JSON Tree Formatter:** Loops over structural indices to write clean, indented tracking syntax blocks (`.json`) complete with comma handling.

---

## 🛠️ OOP Concepts & Architecture Demonstrated

This cybersecurity prototype isolates critical credential items while strictly managing execution permissions:
*   **Classes & Engine Separation:** Decoupled cleanly into independent logical objects: `Credential` (individual entry host) and `PasswordManager` (the tracking engine containing the validation states).
*   **State Control Logic:** Tracks system changes via internal Boolean markers (`is_unlocked`), ensuring structural loops prevent execution breaches if someone bypasses the setup logic.
*   **Relational Dictionaries:** Employs optimized memory mapping by nesting full `Credential` object references directly within hash-map arrays keyed on target website strings.

---

## 🚀 How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd shadow-lock-vault
    ```
3.  **Run the application script:**
    ```bash
    python main.py
    ```

---

## 📝 Prerequisites
*   **Python 3.x** installed on your machine.
*   Runs entirely on pure Python core architecture without needing external library dependencies.
