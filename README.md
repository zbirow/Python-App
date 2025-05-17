# Rename file - Narzędzie do masowej zmiany tekstu w nazwach plików

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)  
![License](https://img.shields.io/badge/License-MIT-green)  
![Encoding](https://img.shields.io/badge/Encoding-UTF--8-orange)```

## 📌 Opis
Aplikacja pozwala na masową zmianę fragmentów tekstu w nazwach plików. Napisana w Pythonie z użyciem `tkinter`.

![Screenshot](https://github.com/zbirow/Rename-file/blob/main/image.png)

## ✨ Funkcjonalności
- Zamiana dowolnego tekstu w nazwach plików
- Obsługa polskich znaków (UTF-8)
- Prosty interfejs graficzny
- Komunikaty o błędach i sukcesie

## ⚙️ Wymagania
- Python 3.x
- Biblioteka `tkinter`

## 🛠️ Instalacja
```bash
# Linux:
sudo apt-get install python3-tk
```
```bush
# Windows/macOS:
pip install tk```
```
## 🚀 Użycie
#1. Uruchom program:
python rename_file.py
lub [rename_file.exe](https://github.com/zbirow/Rename-file/releases "rename_file.exe") z releases

#W interfejsie:

**Kliknij "Wybierz" folder**

**Wpisz tekst do zamiany**

**Kliknij "Zamień tekst"**

#Przykład:
**Stary Tekst:** *old_*
**Nowy Tekst:** *new_*
**Przed:** old_file.txt
**Po**: new_file.txt

## 💾 Kodowanie
Program obsługuje nazwy plików w UTF-8. W przypadku problemów dodaj:
```python
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
```

## ⚠️ Uwagi
- Program nie zmienia zawartości plików
- Działa tylko na plikach, nie na folderach
- W przypadku błędów wyświetla komunikaty
