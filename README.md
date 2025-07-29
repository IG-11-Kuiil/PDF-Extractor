# PDF Extraction Toolkit

A pair of Python scripts for extracting text, tables and OCR‑scanned content from PDFs in Google Colab or any Python environment—all in one place.

---

## Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Note on Hindi OCR](#note-on-hindi-ocr)  
4. [Requirements](#requirements)  
5. [Installation](#installation)  
6. [Usage](#usage)  
   - [Version 1: Digital & Scanned PDF Extraction](#version-1-digital--scanned-pdf-extraction)  
   - [Version 2: Hindi‑Enabled OCR](#version-2-hindi‑enabled-ocr)  
7. [How It Works](#how-it-works)  

---

## Overview

This repository provides two scripts that:

1. Mount your Google Drive.  
2. List all PDFs in `MyDrive`.  
3. Let you select a PDF by its printed index.  
4. For each page:
   - If it contains selectable text, extract paragraphs and any tables.  
   - Otherwise, render it to an image and run OCR.  
5. Save a structured JSON of results back to your Drive.

Version 2 extends Version 1 by passing `lang='hin'` to Tesseract for better Hindi OCR.

---

## Features

- **Digital text extraction** via PyMuPDF (`fitz`)  
- **Table detection & parsing** via Camelot (stream mode)  
- **Scanned‑page OCR** via Tesseract + pdf2image  
- **Google Drive integration**: automatic mount in Colab  
- **JSON output** with page number, type (`digital` vs `scanned`), paragraphs, and tables  
- **Hindi support** in Version 2 (`lang='hin'`)

---

## Note on Hindi OCR

> **English extraction** works reliably for Latin‑script PDFs.  
> **Hindi OCR** (Version 2) may still miss or mis‑recognize some Hindi characters or ligatures—results can vary by document quality.

---

## Requirements

- **Google Colab** or any Ubuntu‑based environment  
- **System packages**:
  - `poppler-utils`
  - `ghostscript`
  - `tesseract-ocr`
  - `tesseract-ocr-hin` (for Hindi)
- **Python packages**:
  - `pymupdf`
  - `pdf2image`
  - `camelot-py[cv]`
  - `pytesseract`

---

## Installation

Run these commands in your Colab cell or terminal:

```bash
# System dependencies
apt-get update && \
apt-get install -y poppler-utils ghostscript tesseract-ocr tesseract-ocr-hin

# Python dependencies
pip install --quiet pymupdf pdf2image camelot-py[cv] pytesseract
