def stringing_methods() :


    # Problem Set 3: String Methods
    # Upper & Lower:
    info = "Python is fun. Fun is good. Good is subjective."
    print("Uppercase:", info.upper()) 
    # Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
    print("Lowercase:", info.lower())
    # String Joining and Splitting:
    # Given the list motto = ["Make", "haste", "slowly."],
    motto = "[Make", "haste", "slowly.]"

    # a. Convert the list into a single string.

    # b. Now, split the string at every occurrence of the letter 'a'.
    reversed_word_positions = info.split()[::-1]
    reversed_word_positions = ' '.join(reversed_word_positions)
    print(reversed_word_positions)