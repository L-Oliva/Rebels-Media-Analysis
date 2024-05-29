# Use a pipeline as a high-level helper
from transformers import pipeline
import glob 
import os 

imagePaths = glob.glob("test/**/*.png",recursive=True)
imagePaths.extend(glob.glob("test/**/*.jpeg",recursive=True))
pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
for i in imagePaths:
    Caption = pipe(i)[0]["generated_text"].strip().replace(" ","_")
    base,ext = i.split(".")
    print(f'{i}: {pipe(i)[0]["generated_text"]}')
    os.rename(i,base+"-"+Caption+"."+ext)

