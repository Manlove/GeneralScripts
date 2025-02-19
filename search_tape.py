#!/opt/homebrew/bin/python3

# Takes a list of tapestation output pdfs and a search term and retuns
# the PDF files where the terms was found.
#
# search_tape.py /home/documents/tapes/*.pdf LIBID

import PyPDF2
import sys
from typing import List

LIBRARY_ID: str = sys.argv[-1]
TAPE_FILES: List[str] = sys.argv[1:-1]

if len(LIBRARY_ID) < 1 or LIBRARY_ID.endswith(".pdf"):
   print(LIBRARY_ID)
   raise ValueError("Please provide a search term")
                    
elif len(TAPE_FILES) < 1:
   raise ValueError("Please provide one or more tapestation pdf files")

else:
   for i in TAPE_FILES:
      with open(i,'rb') as infile:
        pdf_reader = PyPDF2.PdfReader(infile)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        if LIBRARY_ID in text:
           print(i)



