def load_pdf(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text() + " "
    return text

def load_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

file_path = input("Enter file path (PDF or TXT): ")

if file_path.endswith(".pdf"):
    text = load_pdf(file_path)
elif file_path.endswith(".txt"):
    text = load_txt(file_path)
else:
    print("Unsupported file type. Use PDF or TXT.")
    exit()

sentences = nltk.sent_tokenize(text)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(sentences)
