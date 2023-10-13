# Requisites
- **PyCryptoDome**

## Installation
I recommend using a virtual environment to install the dependencies.
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

If not, you can install the dependencies globally.
```bash
pip install -r requirements.txt
```

## Usage
Using files to encrypt and decrypt.

```bash
python3 main.py file_to_encrypt
```

Copy the key after encrypting the file and use it to decrypt the file.

```bash
python3 main.py
Enter key: key
```
