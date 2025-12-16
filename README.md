# CV Parser using Regex and Python

## Project Description
This project is a simple tool to extract important information from unstructured text CVs (resumes) and convert it into **structured data** using **Regular Expressions** and Python.  

The project serves as a **basic step in Natural Language Processing (NLP)** before applying any machine learning models.

---

## Goals
- Extract email addresses  
- Extract phone numbers  
- Extract skills from a predefined list  
- Extract educational qualifications  
- Save results in a **structured JSON file**  
- Display data as a **well-formatted table in the Terminal**

---

## Tools Used
- Python 3.x  
- `re` library for Regex  
- `json` library to save extracted data  
- `tabulate` library to display results in a table in the Terminal  

---

## Project Structure

CV-Parser-Regex-Python/
├── data/sample_cvs/ # Sample CV files
├── src/parser.py # Main parsing code
├── output/parsed_cvs.json # Extracted results
└── README.md # Project description

yaml
نسخ الكود

---

## How to Use

1. Open **CMD** or **PowerShell** and navigate to the project folder:
```bash
cd /d E:\CV-Parser-Regex-NLP
Install the tabulate library if not installed:

bash
نسخ الكود
pip install tabulate
Run the main script:

bash
نسخ الكود
python src\parser.py
After running:

All CVs will be displayed in the Terminal as a well-formatted table

A JSON file output/parsed_cvs.json will be created with all extracted data

Example JSON Output
json
نسخ الكود
[
    {
        "file": "CV_1.txt",
        "emails": ["ahmed.ali@gmail.com"],
        "phones": ["+967777123456"],
        "skills": ["Python", "Machine Learning", "SQL", "NLP"],
        "education": ["Bachelor", "Artificial Intelligence"]
    }
]
Notes
The project uses sample CVs to avoid privacy issues.

Regex is strong for extracting fixed patterns (Email, Phone) but may not catch unusual formats.

The project can be extended later with NLP or machine learning for more advanced text analysis.

git branch -M main
git remote add origin https://github.com/Doaa-ali790/CV-Parser-Regex.git
