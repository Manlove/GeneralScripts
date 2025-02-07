#!/opt/homebrew/bin/python3

# Takes a list of tapestation output pdfs and a search term and retuns
# the PDF files where the terms was found.
#
# search_tape.py /home/documents/tapes/*.pdf LIBID

import PyPDF2, sys

library_id = sys.argv[-1]
tape_files = sys.argv[1:-1]

if len(library_id) < 1 or library_id[-4:] == ".pdf": # change this to "endswith"
   print(library_id)
   raise ValueError("Please provide a search term")
                    
elif len(tape_files) < 1:
   raise ValueError("Please provide one or more tapestation pdf files")

else:
   for i in tape_files:
      with open(i,'rb') as infile:
        pdf_reader = PyPDF2.PdfReader(infile)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        if library_id in text:
           print(i)



