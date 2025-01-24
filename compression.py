def show_menu():
    print("Select an option:")
    print("1. Compress")
    print("2. Decompress")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

def compress(input_text):
    count = 1
    compressed_text = ""
    for i in range(len(input_text) - 1):
        if input_text[i] == input_text[i + 1] and count < 10:
            count += 1
        else:
            compressed_text += str(count)[-1] + input_text[i]
            count = 1
    compressed_text += str(count) + input_text[-1]
    return compressed_text

def decompress(compressed_text):
    decompressed_text = ""
    i = 0
    while i < len(compressed_text):
        count = int(compressed_text[i])
        char = compressed_text[i + 1]
        if (count != 0):
            decompressed_text += char * count
        else:
            decompressed_text += char * 10
        i += 2
    return decompressed_text


while (choice := show_menu()) != "3":
    if choice == "1":
        print(compress(input("Enter the text to compress: ")))
    elif choice == "2":
        print(decompress(input("Enter the text to decompress: ")))
    else:
        print("Invalid choice, please try again.")
