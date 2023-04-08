import openai
import PyPDF2

# Set up the OpenAI API key
openai.api_key = "inputAPIhere"

# Open the PDF file in read-binary mode
with open('study.pdf', 'rb') as file:
    # Create a PDF reader object
    reader = PyPDF2.PdfReader(file)

    # Extract the text from the PDF file
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    # Split the text into paragraphs based on newline character
    paragraphs = text.split('\n\n')

    # Create an empty list to store the words
    words_list = []

    # Iterate over each paragraph
    for paragraph in paragraphs:
        # Remove spaces between characters in each line
        line = paragraph.replace(" ", "")

        # Split the line into words based on uppercase characters
        words = []
        word = ""
        for char in line:
            if char.isupper() and word != "":
                words.append(word)
                word = ""
            word += char
        if word != "":
            words.append(word)

        # Add the words to the list
        words_list.extend(words)
        words_list = [word.replace('\n', '') for word in words_list]
        words_list = [word.replace('.', '') for word in words_list]
        words_list = [word.replace(';', '') for word in words_list]
        words_list = [word.replace('(', '') for word in words_list]
        words_list = [word.replace(',', '') for word in words_list]
        words_list = [word.replace(')', '') for word in words_list]
        words_list = [word.replace('-', '') for word in words_list]

    # Remove single character items from the list
    words_list = [word for word in words_list if len(word) > 1]

    # Use OpenAI to search each word and get its definition
    with open('definitions.txt', 'w') as f:
        for word in words_list:
            definition = openai.Completion.create(
                engine="text-ada-001",
                prompt=f"Define {word}.",
                max_tokens=70,
                n=1,
                stop=None,
                temperature=0.5,
            ).choices[0].text
            f.write(f"{word}:{definition}\n-------------------------------------------------\n")
