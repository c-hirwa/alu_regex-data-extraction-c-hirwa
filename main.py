import re

def load_sample_text(filename):
    with open(filename, 'r') as file:
        return file.read()
    
#Regex function to filter needed elements