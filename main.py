from ocr import extract_text
from risk import analyze_text
from fastapi import FastAPI,UploadFile,File
import shutil
import os
UPLOAD_DIR="uploads"
os.makedirs(UPLOAD_DIR,exist_ok=True)
app=FastAPI()

@app.post("/analyze")
async def analyze(file:UploadFile=File(...)):
    path=os.path.join(UPLOAD_DIR,file.filename)
    with open(path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    text=extract_text(path)
    result=analyze_text(text)
    return{
        "extracted_text":text,
        "privacy_score":result["score"],
        "risks":result["risks"]
    }

