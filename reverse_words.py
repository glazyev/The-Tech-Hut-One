def message_encoder(message):
    """Takes a sentence and reverses the order of words and characters
    Takes a sentence as an argument
    Returns a string with reversed order of words and characters
    """
    #reverse order of words
    reversed_words =message.split()[::-1]

    #reverse order of letters
    reversed_letters = []
    for word in reversed_words:
        reversed_letters.append(word[::-1])

    #join to form encoded message
    encoded_message = " ".join(reversed_letters)

    return encoded_message

message = input("Enter a message to be encoded: ")
encoded_message = message_encoder(message)
print("Encoded Message is : ", encoded_message)