# CaféLibro - Library Loan Manager

A simple digital tool for a library to run its book lending from the terminal. This command-line program keeps track of books in the catalogue, registered members, and active loans, storing all data in a shared JSON file.

## 🛠️ Features and Owners

As required, here is the distribution of the application's features among the team members:

* **1. Register a member**, with a name and a unique identifier. -> **Eimmy Ochoa**
* **2. Loan a book to a member**. -> **José Toapanta**
* **3. Return a book**, marking it available again. -> **Sebastian Holguin**
* **4. List the books** a member currently has on loan. -> **Issac Maza**
* **5. Report the loans that are overdue**. -> **Leonardo Zambrano**

## 🚀 Continuous Integration

This repository implements a Continuous Integration pipeline using GitHub Actions. 
* The workflow automatically runs the test suite on every push and pull request to the `main` branch. 
* The `main` branch is protected: the build must pass and require at least one approving review before any merge.