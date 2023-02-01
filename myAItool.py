#!/usr/bin/env python3
"""
this AI tool uses regular expressions to check for specific writing issues and make replacements.
The writing_enhancement_tool function checks for grammatical errors, spelling mistakes, and other writing issues. 
The calculation_enhancement_tool function takes a calculation expression as input and returns the result of the calculation or an error message if 
the expression is invalid
"""
import re

def writing_enhancement_tool(text):
    # Check for grammatical errors
    text = re.sub(r'your', 'you\'re', text)
    text = re.sub(r'its', 'it\'s', text)
    text = re.sub(r'there', 'they\'re', text)
    text = re.sub(r'too', 'two', text)
    text = re.sub(r'loose', 'lose', text)

    # Check for spelling mistakes
    text = re.sub(r'colour', 'color', text)
    text = re.sub(r'centre', 'center', text)
    text = re.sub(r'favour', 'favor', text)
    text = re.sub(r'licence', 'license', text)

    # Check for other writing issues
    text = re.sub(r'\bi\b', 'I', text)
    text = re.sub(r'(\w)\1{2,}', r'\1\1', text)

    return text

def calculation_enhancement_tool(expression):
    try:
        result = eval(expression)
    except:
        result = "Invalid expression"

    return result

text = input("Enter your text: ")
print("Writing enhancement result: ", writing_enhancement_tool(text))

expression = input("Enter a calculation expression: ")
print("Calculation enhancement result: ", calculation_enhancement_tool(expression))
