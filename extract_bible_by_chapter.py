import json
import re
import os

os.mkdir("by_chapter")

with open("json/ESV.json") as file:
    data = json.load(file)
    books = data["books"]

book_index = 1
for book_title in books:
    file_title = str.replace(book_title, " ", "_")
    file_title = f"{book_index:02d}_{file_title}"
    book = books[f"{book_title}"]
    chapters = [chapter for chapter in book]
    os.mkdir(f"by_chapter/{file_title}")
    fulltexts = []

    chap_index = 1
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

        with open(f"by_chapter/{file_title}/Chapter_{chap_index:02d}.md", "w") as file:
            for chapter in fulltexts:
                file.write(f"# Chapter {chap_index}\n\n")
                verse_index = 1
                for verse in chapter:
                    file.write(f"{verse_index}. {verse}\n")
                    verse_index += 1
                file.write("\n")
        chap_index += 1
    book_index += 1
