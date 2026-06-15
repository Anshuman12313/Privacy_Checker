import re
def analyze_text(text):
    risks=[]

    phone_pattern=r'\b[6-9]\d{9}\b'
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    aadhaar_pattern = r'\b\d{4}\s?\d{4}\s?\d{4}\b'

    Score=100

    if re.search(phone_pattern,text):
        risks.append("Phone Number")
        Score-=20
    
    if re.search(email_pattern,text):
        risks.append("Email")
        Score-=20

    if re.search(aadhaar_pattern,text):
        risks.append("Adhaar Number")
        Score-=20

    return {
        "score":Score,
        "risks":risks
    }
    


