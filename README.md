# QR Code Validator

A Python project for reading, comparing, and validating QR-code data represented as binary text matrices. 

## Overview

This project models QR-code data using Python classes and helper functions. It loads binary matrices from text files, stores QR-code metadata, compares datasets, and checks whether differences exceed a specified error-correction tolerance.

**Note:** This is a validator for text-based QR-code representations, not a tool for generating or scanning QR-code images.

## Features

- Read binary QR-code matrices from text files.
- Represent matrix data using the `TxtData` class.
- Store QR-code ownership, last-update date, and error-correction metadata in a `QRCode` object.
- Compare QR codes for exact equality.
- Check whether a QR code is corrupted relative to a reference, using an allowed tolerance.
- Work with sample files for matching and altered data.

## Project structure

| File | Purpose |
| --- | --- |
| `qrcode.py` | `QRCode` class and QR-code comparison/validation logic |
| `txtdata.py` | `TxtData` class for working with text-based matrix data |
| `helper.py` | Helper functions for reading data and converting dates |
| `qrcode_binary.txt` | Sample QR-code matrix |
| `qrcode_binary_copy.txt` | Sample copy for comparison |
| `qrcode_binary_error.txt` | Altered QR-code sample |
| `small_data.txt` | Small sample dataset |
| `small_data_error.txt` | Altered small dataset |

## How to run the code

### 1. Download the project

Open a terminal and run:

```bash
git clone https://github.com/rashahaidar0/QR-Code.git
cd QR-Code
```

Alternatively, on GitHub click **Code → Download ZIP**, extract the ZIP, and open the extracted folder in VS Code.

### 2. Check that Python is installed

Run:

```bash
python3 --version
```

The project uses Python 3 and local modules; no external packages are documented.

### 3. Open Python from the project folder

In the terminal, run:

```bash
python3
```

Then enter the following commands in the Python prompt:

```python
from qrcode import QRCode

original = QRCode("qrcode_binary.txt", "01/01/2024", "Example", 0.1)
copy = QRCode("qrcode_binary_copy.txt", "01/01/2024", "Example", 0.1)

print(original)
print(original.equals(copy))
print(copy.is_corrupted(original))
```

These commands create two QR-code objects from the included sample text files, compare them, and check for corruption. The constructor arguments are the file path, last-update date (`DD/MM/YYYY`), owner, and error-correction tolerance.

To leave Python, type `exit()`.

**Important:** `qrcode.py`, `txtdata.py`, `helper.py`, and the sample `.txt` files should remain together in the project folder. This repository defines reusable classes rather than a standalone command-line application, so running `python3 qrcode.py` by itself may not display any results.

## How validation works

The program loads each QR code as a matrix of binary values. `equals()` checks whether two QR codes have matching matrix data and error-correction settings. `is_corrupted(reference)` compares a QR code against a reference using the reference's allowed error-correction tolerance.

## Technologies and concepts

**Language:** Python 3  
**Concepts:** Object-oriented programming, file I/O, 2D arrays, input validation, data comparison, and error handling.

## Background

Developed for **COMP 202 at McGill University** as a programming assignment focused on working with structured data and object-oriented design.
