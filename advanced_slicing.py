def advanced_slice() :

    # Advanced Slicing:
    # Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # a. Extract the letters 'hij' #hij_index = alphabet.index('hij')
    print(alphabet[7:10])
    # b. Extract every second letter starting from 'a' to 'm'.
    extracted_letters = alphabet[1::2]
    print(extracted_letters)