# Matrix Calculator

A simple command-line matrix calculator written in Python with NumPy.

## Features

- Matrix addition
- Matrix subtraction
- Matrix multiplication
- Matrix transpose
- Determinant calculation
- Matrix inverse calculation

## Requirements

- Python 3.11
- NumPy

## Installation

Create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Usage

Run the calculator with:

```powershell
python .py
```

Choose an operation from the menu and enter matrices as Python-style nested lists. For example:

```text
[[1, 2], [3, 4]]
```

The selected operation must be mathematically valid for the entered matrices. Determinant and inverse require a square matrix, and an inverse requires a non-singular matrix.

## Notes

This program currently uses `eval()` to parse matrix input. Use it only with trusted input.
