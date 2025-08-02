# Pension Management System

A simple Python-based pension database system using MySQL. It generates mock pension data (including names, birthdates, account numbers, and pension amounts) and allows basic operations like viewing, adding, or deleting records.

---

## 📦 Project Contents

- `CREATE_DATABASE.py` - Generates synthetic data and creates a MySQL database with pension records.
- `EDITOR.py` - Provides a command-line interface to view, add, or delete entries in the pension table.
- `name.txt` & `surnames.txt` - Lists of first names and surnames used to generate full names.

---

## 🔧 Features

- Randomized data generation:
  - Indian-style bank account numbers
  - Random names from provided name files
  - Date of birth and pension calculation
- MySQL integration for persistent storage
- CLI interface for:
  - Viewing all records
  - Deleting records by name
  - Appending new entries manually

---

## 🛠 Requirements

- Python 3.x
- `mysql-connector-python` (Install via `pip install mysql-connector-python`)
- MySQL server running on `localhost` with a root account

---

## 🚀 Getting Started

### 1. Generate & Create Database
```bash
python CREATE_DATABASE.py

python EDITOR.py
```

## Files

| File              | Description |
|-------------------|-------------|
| `CREATE_DATABASE.py` | Generates pensioner data and creates a MySQL database table `PensionData` with the generated records. |
| `EDITOR.py`          | Provides a CLI to view, add, or delete records from the `PensionData` table. |
| `name.txt`           | List of sample first names used for generating fake names. |
| `surnames.txt`       | List of sample surnames used for generating fake names. |
---
## 🗃 Database Table Structure

Table: `PensionData`

| Column         | Type         |
|----------------|--------------|
| account_number | VARCHAR(64)  |
| dob            | DATE         |
| name           | VARCHAR(64)  |
| pension        | INT          |

---
Notes

Pension is calculated based on year of birth (assuming retirement age is 60).

Generated account numbers are random but follow a pattern based on a list of fake bank codes.

Ensure MySQL server is running locally and accessible to root with the password you provide.
