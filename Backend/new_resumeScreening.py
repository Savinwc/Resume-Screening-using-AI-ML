from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
nltk.download('punkt')

import input_skills
import skills_matching

output_string = StringIO()
with open('D:\python\mini_project\Aaron Pereira Resume (1).pdf', 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)


# print(output_string.getvalue()) #Output_string.getvalue() prints the whole text that is converted from pdf

pdf_text = output_string.getvalue() # storing the converted text in the pdf_text variable

pdf_text = pdf_text.lower() # making the whole text to lowercase which makes it easy to understand

token_word = word_tokenize(pdf_text) #word_tokenize tokenizes the text and tokenized text is stored in token_word
# print(token_word)
# sw = stopwords.words('english')
# text = {w for w in token_word if not w in sw} 
# print(text)
company_skills = []

company_skills.extend(input_skills.get_tech_skills_data())
company_skills.extend(input_skills.get_soft_skills_data())
com_percentage = int(input("Enter the minimum eligibilty criteria:"))

print(company_skills)
skills_matched = []
skills_matched = skills_matching.skills(company_skills, token_word)
# print(skills_matched)
# print(len(skills_matched))
# print(len(company_skills)) 
def prob(n,m=1):
    pro = n/m
    return pro*100

pro = prob(skills_matched[0],len(company_skills))
print("The skills matched are")
print (pro,"%")

if (com_percentage == pro or com_percentage <= pro):
    print("The resume is accepted!")
else:
    print("The resume does not match comapny requirements") 