import PyPDF2

# Create an empty list to store the words
words_list = []

# Open the PDF file in read-binary mode
with open('study.pdf', 'rb') as file:
    # Create a PDF reader object
    reader = PyPDF2.PdfReader(file)

    # Iterate over each page in the PDF file
    for page in reader.pages:
        # Extract the text from the page
        text = page.extract_text()

        # Split the text into sentences using period as delimiter
        sentences = text.split('.')

        # Iterate over each sentence
        for sentence in sentences:
            # Split the sentence into words
            words = sentence.split()

            # Append the words to the list
            words_list.extend(words)

            # Print the sentence if it contains any words
            if len(words) > 0:
                # Concatenate the words and the period to form the sentence
                sentence = ''.join(words) + '.'
                print(sentence.strip())

# Print the list of words
print(words_list)
