def word_searching() :

    # Word Search:
    # Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
    text = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
    word_to_find = "moonlight"

    if word_to_find.lower() in text.lower():
        print(f'The word "{word_to_find}" appears in the quote.')
    else:
        print(f'The word "{word_to_find}" does not appear in the quote.')