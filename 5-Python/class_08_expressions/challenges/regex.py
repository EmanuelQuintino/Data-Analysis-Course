import re

text = '''
Regular expressions (called REs, or regexes, or regex patterns) are essentially a tiny, highly specialized programming language embedded inside Python and made available through the re module. Using this little language, you specify the rules for the set of possible strings that you want to match; this set might contain English sentences, or e-mail addresses, or TeX commands, or anything you like. You can then ask questions such as "Does this string match the pattern", or "Is there a match for the pattern anywhere in this string". You can also use REs to modify a string or to split it apart in various ways.
'''

# Quantas vezes a letra "a" aparece no texto?
print(len(re.findall("a", text)))
print(text.count("a"))

# Quantas vezes a palavra "you" aparece no texto?
print(len(re.findall(r"\byou\b", text, re.IGNORECASE)))
print(text.lower().count("you"))

# Recupere todas as palavras que terminam em "."
print(text.lower().count("?"))
print(len(re.findall("\?", text)))
print(re.findall(r"\b\w+\?", text))

# Recupere todas as expressões que estão entre aspas duplas("")
print(re.findall(r'"(.*?)"', text))
