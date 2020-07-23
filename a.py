# import spacy

# # Load the large English NLP model
# nlp = spacy.load('en_core_web_lg')

# # The text we want to examine
# text = """London is the capital and most populous city of England and 
# the United Kingdom.  Standing on the River Thames in the south east 
# of the island of Great Britain, London has been a major settlement 
# for two millennia. It was founded by the Romans, who named it Londinium.
# """

# # Parse the text with spaCy. This runs the entire pipeline.
# doc = nlp(text)

# # 'doc' now contains a parsed version of text. We can use it to do anything we want!
# # For example, this will print out all the named entities that were detected:
# for entity in doc.ents:
#     print(f"{entity.text} ({entity.label_})")


# import spacy

# # Load the large English NLP model
# nlp = spacy.load('en_core_web_lg')

# # Replace a token with "REDACTED" if it is a name
# def replace_name_with_placeholder(token):
#     if token.ent_iob != 0 and token.ent_type_ == "PERSON":
#         return "[REDACTED] "
#     else:
#         return token.string

# # Loop through all the entities in a document and check if they are names
# def scrub(text):
#     doc = nlp(text)
#     for ent in doc.ents:
#         ent.merge()
#     tokens = map(replace_name_with_placeholder, doc)
#     return "".join(tokens)

# s = """
# In 1950, Alan Turing published his famous article "Computing Machinery and Intelligence". In 1957, Noam Chomsky’s 
# Syntactic Structures revolutionized Linguistics with 'universal grammar', a rule based system of syntactic structures.
# """

# print(scrub(s))


import spacy
import textacy.extract

# Load the large English NLP model
nlp = spacy.load('en_core_web_lg')

# The text we want to examine
text = """London is [.. shortened for space ..]"""

# Parse the document with spaCy
doc = nlp(text)

# Extract noun chunks that appear
noun_chunks = textacy.extract.noun_chunks(doc, min_freq=3)

# Convert noun chunks to lowercase strings
noun_chunks = map(str, noun_chunks)
noun_chunks = map(str.lower, noun_chunks)

# Print out any nouns that are at least 2 words long
for noun_chunk in set(noun_chunks):
    if len(noun_chunk.split(" ")) > 1:
        print(noun_chunk)