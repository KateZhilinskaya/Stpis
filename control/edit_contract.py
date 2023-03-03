import re
from docx import Document
from django.conf import settings
from datetime import datetime as dt
import os


def template_contract(filename, string, new_string):
    document = Document(f"{settings.BASE_DIR}/static/contracts/{filename}")
    for p in document.paragraphs:
        for run in p.runs:
            if run.text:
                replaced_text = re.sub(string, new_string, run.text, 999)
                if replaced_text != run.text:
                    run.text = replaced_text

    os.chdir(r"D:\курсовая СТПИС\zhilinskaya-main\media\contracts")

    new_filename = str(dt.now().strftime("%d-%m-%y-%H:%M:%S")) + "-" + str(filename)
    document.save(rf"D:\курсовая СТПИС\zhilinskaya-main\media\contracts\{new_filename.split('.')[0]}.docx")
    return rf"D:\курсовая СТПИС\zhilinskaya-main\media\contracts\{new_filename.split('.')[0]}.docx"
