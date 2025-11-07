def extracted_information() :


    # Problem Set 2: Extracting Information
    # From Descriptions:
    # Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
    quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
    print(quote[-16: ])

    info = "Python is fun. Fun is good. Good is subjective."
    start_index = info.find('subjective')
    if start_index != -1:
        end_index = start_index + len('subjective')
        word = info[start_index:end_index]
        print(word)
    # b. Extract every third word.
    words_list = info.split()
    third_words = words_list[2::3]
    print(f"Original sentence: {info}")
    print(f"List of words: {words_list}")
    print(f"Every third word: {third_words}")
    # c. Reverse the positions of the words, but keep the characters in each word in the same order.
    reversed_string = words_list[::-1]