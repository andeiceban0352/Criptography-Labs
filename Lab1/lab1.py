ALPHABET  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_shiftedalphabet(key):
    curr_alphabet = ALPHABET
    unique_chars_list = ""
    for char in key:
        if char not in unique_chars_list:
            unique_chars_list += char

    shifter_list = unique_chars_list #le pune primele , apoi le adauga pe restul
    for char in curr_alphabet:
        if char not in unique_chars_list:
            shifter_list += char

    return shifter_list

def cezar_encript(message, key1, key2 = None):
    curr_alphabet = ALPHABET
    if key2 is None:
        rez = ""
        for char in message:
            index = curr_alphabet.index(char)
            letter = (index + key1) % 26
            rez += curr_alphabet[letter]
        return rez
    else:
        encripted_text = ""
        for char in message:
            index = curr_alphabet.index(char)
            letter = (index + key1) % 26
            encripted_text += curr_alphabet[letter]
        rez = ""
        shifted_alphabet = get_shiftedalphabet(key2)
        for char in encripted_text:
            index = curr_alphabet.index(char)
            rez  += shifted_alphabet[index]
        return rez



def cezar_decript(message, key1, key2 = None):
    curr_alphabet = ALPHABET
    if key2 is None:
        rez = ""
        for char in message:
            index = curr_alphabet.index(char)
            letter = (index - key1) % 26
            rez += curr_alphabet[letter]
        return rez
    else:
        shifted_alphabet = get_shiftedalphabet(key2)
        message_2 = ""
        for char in message:
            index = shifted_alphabet.index(char)
            message_2 += curr_alphabet[index]
        
        rez = ""
        for char in message_2:
            index = curr_alphabet.index(char)
            letter = (index - key1) % 26
            rez += shifted_alphabet[letter]
        return rez


def display_menu():
    print("Chose the operation:")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")


def main():
    global rez

    while True:
        display_menu()

        choice = input("Make a choice: ")

        if choice == '1':
            message = str(input('Enter the message to encript : '))
            message = message.replace(" ", "").upper()

            for char in message:
                if char not in ALPHABET:
                    print(f"Invalid character '{char} in the message. You must input just latin alphabet letters")
                    continue


            key1 = int(input("Enter the encript key : "))
            if not 1 <= key1 <= 25:
                print("Wrong key. Enter a value between 1 and 25")
                continue
            
            key2 = str(input('Enter the second key (optionl) : '))
            key2 = key2.replace(" ", "").upper()

            chars = 0
            for char in key2:
                if char.isalpha(): 
                    chars = 1
                    break
                else:
                    chars = 0
            if chars == 0:
                key2 = None

            if key2 is None:
                encripted_message = cezar_encript(message, key1, key2)
                print("The encrypted message with 1 key is:", encripted_message)
            else:

                if(len(key2) < 7):
                    print("The key must have at least 7 characters.")
                    continue
                for char in key2:
                    if char not in ALPHABET:
                        print(f"Invalid character '{char} in the message. You must input just latin alphabet letters")
                        continue
                
                encripted_message = cezar_encript(message, key1, key2)
                print("The encrypted message with 2 keys is:", encripted_message)
                print("The shifted alphabet is : " , get_shiftedalphabet(key2))
                
        
        elif choice == '2':
            message = str(input('Enter the message to decript : '))
            message = message.replace(" ", "").upper()
            
            key1 = int(input("Enter decription key : "))
            if not 1 <= key1 <= 25:
                print("Wrong key. Enter a value between 1 and 25")
                continue

            for char in message:
                if char not in ALPHABET:
                    print(f"Invalid character '{char} in the message. You must input just latin alphabet letters")
                    continue

          
            key2 = str(input('Enter the second key (optionl) : '))
            key2 = key2.replace(" ", "").upper()

            chars = 0
            for char in key2:
                if char.isalpha(): 
                    chars = 1
                    break
                else:
                    chars = 0
            if chars == 0:
                key2 = None

            if key2 == None:
                decripted_message = cezar_encript(message, key1, key2)
                print("The decripted message with 1 key is:", decripted_message)

            else:
                if(len(key2) < 7):
                    print("The key must have at least 7 characters.")
                    continue
                for char in key2:
                    if char not in ALPHABET:
                        print(f"Invalid character '{char} in the message. You must input just latin alphabet letters")
                        continue

                decripted_message = cezar_decript(message, key1, key2)
                print("The decripted message with 2 keys is:", decripted_message)
                print("The shifted alphabet is : " , get_shiftedalphabet(key2))
            
        elif choice == "3":
            break
        else:
            print("Invalid choice . Try again")

if __name__ == "__main__":
    rez = ""
    main()


