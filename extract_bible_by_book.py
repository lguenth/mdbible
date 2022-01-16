import json
import re
import os

os.mkdir("by_book")
with open("json/ESV.json") as file:
    data = json.load(file)
    books = data["books"]

book_index = 1
for book_title in books:
    file_title = str.replace(book_title, " ", "_")
    file_title = f"{book_index:02d}_{file_title}"
    book = books[f"{book_title}"]
    chapters = [chapter for chapter in book]
    fulltexts = []

    for chapter in chapters:
        verses = [verse for verse in chapter]
        indeces = [verses.index(verse) for verse in chapter]

        verses = []

        for index in indeces:
            chunks = [i for i in chapter[index]]
            verse = " ".join([chunk[0]
                              for chunk in chunks if not isinstance(chunk[0], list)])
            verse = re.sub(r'\s([?.,;!"](?:\s|$))', r'\1', verse)
            verses.append(verse)

        fulltexts.append(verses)

    with open(f"by_book/{file_title}.md", "w") as file:
        file.write(f"# {book_title}\n\n")
        chap_index = 1
        for chapter in fulltexts:
            file.write(f"## Chapter {chap_index}\n\n")
            verse_index = 1
            for verse in chapter:
                file.write(f"{verse_index}. {verse}\n")
                verse_index += 1
            file.write("\n")
            chap_index += 1
    book_index += 1
