# PDF Extraction Toolkit

A pair of Python scripts for extracting text, tables and OCR‑scanned content from PDFs in Google Colab or any Python environment.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
  - [Version 1: Digital & Scanned PDF Extraction](#version-1)  
  - [Version 2: Hindi‑Enabled OCR](#version-2)  
- [How It Works](#how-it-works)  
- [Troubleshooting & Notes](#troubleshooting--notes)  
- [License](#license)  

---

## Overview

This repo contains two scripts that mount your Google Drive, list PDFs, let you select one by index, then:

- **Detects** whether each page is “digital” (extractable text) or a scanned image.  
- **Extracts** paragraphs and any tabular data (via Camelot).  
- **Runs** Tesseract OCR on scanned pages to pull out text.

Version 2 extends Version 1 by specifying `lang='hin'` in `pytesseract` to improve extraction from Hindi documents.

---

## Features

- **Digital text extraction** via PyMuPDF  
- **Table detection & parsing** via Camelot (stream flavor)  
- **Scanned‑page OCR** via Tesseract + pdf2image  
- **Drive integration**: automatically mounts your Google Drive in Colab  
- **JSON output**: saves a structured array of pages, types, paragraphs, tables  

Version 2 adds:

- **Hindi OCR**: passes `lang='hin'` to Tesseract for better Devanagari support  

---

## Requirements

- **Linux / Colab environment**  
- Apt packages:  
  - `poppler-utils`  
  - `ghostscript`  
- Python packages:  
  - `pymupdf`  
  - `pdf2image`  
  - `camelot-py[cv]`  
  - `pytesseract`  

Make sure you also install the Hindi language pack for Tesseract:

```bash
sudo apt-get install tesseract-ocr-hin

