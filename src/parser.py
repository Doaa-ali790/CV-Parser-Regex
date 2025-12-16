import re
import os
import json

# ------------------ تعاريف Regex ------------------
EMAIL_REGEX = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
PHONE_REGEX = r'(\+?\d{1,3}[-\s]?)?(\(?\d{2,3}\)?[-\s]?)?\d{3,4}[-\s]?\d{3,4}'
EDUCATION_REGEX = r'Bachelor|Master|PhD|Information Technology|Computer Science|Artificial Intelligence'
# قائمة مهارات يمكن تعديلها بسهولة
SKILLS_LIST = ['Python', 'Machine Learning', 'SQL', 'NLP', 'Pandas', 'Data Analysis', 'Deep Learning', 'Java', 'Databases']

# ------------------ دوال استخراج ------------------
def extract_email(text):
    return re.findall(EMAIL_REGEX, text)

def extract_phone(text):
    phones = re.findall(PHONE_REGEX, text)
    # دمج tuples الناتجة إلى string
    return [''.join(p) for p in phones]

def extract_education(text):
    match = re.findall(EDUCATION_REGEX, text, re.IGNORECASE)
    return match if match else []

def extract_skills(text):
    found_skills = []
    for skill in SKILLS_LIST:
        if re.search(r'\b' + re.escape(skill) + r'\b', text, re.IGNORECASE):
            found_skills.append(skill)
    return found_skills

# ------------------ قراءة ملفات CV ------------------
cv_folder = 'data/sample_cvs'
parsed_data = []

for file in os.listdir(cv_folder):
    file_path = os.path.join(cv_folder, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    cv_info = {
        'file': file,
        'emails': extract_email(text),
        'phones': extract_phone(text),
        'skills': extract_skills(text),
        'education': extract_education(text)
    }
    
    parsed_data.append(cv_info)

# ------------------ حفظ النتائج في JSON ------------------
output_folder = 'output'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

output_file = os.path.join(output_folder, 'parsed_cvs.json')
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(parsed_data, f, indent=4)

print(f"✅ تم تحليل جميع السير الذاتية وحفظ النتائج في {output_file}")
