import asyncio
import json
from utils import frequency

f    = open("langs.json", "r")
json = json.loads(f.read())
freq = frequency("textStatIn.txt")

async def compare(language, frequency):
    total = 0
    for letter in json[language]:
        if letter not in frequency:
            frequency[letter] = 0
        total += abs(frequency[letter] - float(json[language][letter]))

    return total

loop = asyncio.get_event_loop()

langs = [

    "English",
    "French",
    "German",
    "Spanish",
    "Portuguese",
    "Esperanto",
    "Italian",
    "Turkish",
    "Swedish",
    "Polish",
    "Dutch",
    "Danish",
    "Icelandic",
    "Finnish",
    "Czech"

]

tasks = [asyncio.ensure_future(compare("English", freq)),
            asyncio.ensure_future(compare("French", freq)),
            asyncio.ensure_future(compare("German", freq)),
            asyncio.ensure_future(compare("Spanish", freq)),
            asyncio.ensure_future(compare("Portuguese", freq)),
            asyncio.ensure_future(compare("Esperanto", freq)),
            asyncio.ensure_future(compare("Italian", freq)),
            asyncio.ensure_future(compare("Turkish", freq)),
            asyncio.ensure_future(compare("Swedish", freq)),
            asyncio.ensure_future(compare("Polish", freq)),
            asyncio.ensure_future(compare("Dutch", freq)),
            asyncio.ensure_future(compare("Danish", freq)),
            asyncio.ensure_future(compare("Icelandic", freq)),
            asyncio.ensure_future(compare("Finnish", freq)),
            asyncio.ensure_future(compare("Czech", freq))
        ]

a = loop.run_until_complete(asyncio.gather(*tasks))
print(a)
print("Lingua rilevata: " + str(langs[a.index(min(a))]) + ", percentuale: " + str(min(a)))
loop.close()
