# Package Sorter

This project contains a Python function for sorting packages based on their dimensions and weight, as required by Thoughtful’s robotic automation system.

## 📦 Objective

Classify packages into appropriate stacks based on these rules:

- **Bulky**: Volume ≥ 1,000,000 cm³ **or** any dimension ≥ 150 cm.
- **Heavy**: Mass ≥ 20 kg.

### Stack Categories

- `STANDARD`: Neither bulky nor heavy.
- `SPECIAL`: Either bulky or heavy.
- `REJECTED`: Both bulky **and** heavy.

## 🚀 Usage

Run `main.py` to test the function. It includes 9 assert-based test cases covering:

- 3 `STANDARD` cases
- 3 `SPECIAL` cases
- 3 `REJECTED` cases

```bash
python main.py
