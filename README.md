# py-language-guesser
First little Python project for school purposes. It guesses the language of the given text
<br>
It guesses the language of the text contained in textStatIn.txt

# What is the purpose of the .js file?
`decode.js` is used to generate an object from a Wikipedia article that contains letters frequency by language (https://wikipedia.org/Letter_Frequency)<br>

# How does it work
Given a certain percentage of all the letters in a text (and using the file `langs.json` which has been generated through `decode.js`) the script can guess the language in which the text is written.
<br>
__Example__:
- The 8% of the letters in an English text is averagely "a"s, the 1% is "b"s and so on...
- Using this kind of logic the script can guess the language.
