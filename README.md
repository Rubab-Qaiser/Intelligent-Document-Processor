# Intelligent Document Processing

A FastAPI-based OCR and document extraction API that classifies documents and extracts dates, amounts, and entities from scanned receipts or other images.

## Features
- OCR using Tesseract
- Document classification using pre-trained `joblib` model files
- Date, amount, and entity extraction using regex and spaCy
- FastAPI endpoints for classification, extraction, and combined processing

## Requirements
- Python 3.12+
- Tesseract OCR installed on Windows
- Python packages listed in `requirements.txt`

## Setup
1. Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
2. Install Python dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Install Tesseract OCR for Windows:
   - Download from https://github.com/UB-Mannheim/tesseract/wiki
   - Install and make sure `tesseract.exe` is on your PATH

## Running the API
```powershell
cd C:\Users\PMLS\Downloads\Intelligent_Document_Processing
uvicorn main:app --reload
```

Then open the API docs at:

```
http://127.0.0.1:8000/docs
```

## Project structure
- `main.py` - FastAPI application
- `extractors.py` - extraction helper functions
- `requirements.txt` - Python dependencies
- `.gitignore` - ignored files for git

## Notes
- If Tesseract is not on the system PATH, `main.py` is configured to use `C:\Program Files\Tesseract-OCR\tesseract.exe`.
- The model files `vectorizer.pkl` and `classifier.pkl` must be present in the project folder.
