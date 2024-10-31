# GPG Encryptor

Welcome to the GPG Encryptor project! This repository contains a command-line interface (CLI) and a graphical user
interface (GUI) for encrypting files using GPG.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
    - [CLI Usage](#cli-usage)
    - [GUI Usage](#gui-usage)
- [License](#license)

## Overview

The GPG Encryptor provides an easy way to encrypt files using GPG. You can use either the command-line interface or the
graphical user interface to encrypt your files securely.

## Installation

Before you start, ensure that you have GPG installed on your system. You can download it
from [GPG official site](https://gnupg.org/download/).

### Clone the Repository

```
git clone https://github.com/NitroStar654/gpg-encryptor.git
cd gpg-encryptor
```

### Install Dependencies

The CLI and GUI are built using Python. Install the required dependencies using pip:

```
pip install -r requirements.txt
```

## Usage

### CLI Usage

The CLI allows you to encrypt files directly from the command line.

#### Running the CLI

```
python cli.py <input_file> <output_file> <recipient_email>
```

#### Example:
```
python cli.py secret.txt secret.txt.gpg recipient@example.com
```

### GUI Usage

The GUI provides a user-friendly interface for encrypting files.

#### Running the GUI

```
python gui.py
```

#### Using the GUI

Input File: Click "Browse" to select the file you want to encrypt.\
Output File: Click "Save As" to choose the destination and name for the encrypted file.\
Recipient Email: Enter the email address associated with the recipient's GPG key.
Click "Encrypt" to encrypt the file.

## License

This project is licensed under the MIT Licence. See the [LICENSE](LICENSE) file for details.

---

We hope you find the GPG Encryptor useful! If you have any questions or encounter any issues, feel free to open an issue
on GitHub.

---
