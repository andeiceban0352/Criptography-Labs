def validate_input(message):
    alphabet_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ")
    if not set(message).issubset(alphabet_chars):
        print("Textul trebuie să conțină doar litere și spații.")
        return False
    return True

def vigenere_algorithm(message, key, operation):
    message = message.replace(" ", "").upper()
    key = key.upper()
    key_len = len(key)
    result = []

    for index, char in enumerate(message):
        if char == ' ':
            result.append(' ')
        else:
            if operation == 'criptare':
                shift = (ord(char) - ord('A') + ord(key[index % key_len]) - ord('A')) % 26
            elif operation == 'decriptare':
                shift = (ord(char) - ord('A') - (ord(key[index % key_len]) - ord('A'))) % 26

            new_char = chr(shift + ord('A'))
            result.append(new_char)

    return ''.join(result)

def main():
    print("Introduceti criptare/decriptare ")
    while True:
        operation = input("Selectați operația (criptare/decriptare): ").lower()
        if operation not in ['criptare', 'decriptare']:
            print("Operație invalidă. Vă rugăm să selectați criptare sau decriptare.")
            continue

        key = input("Introduceți cheia : ")
        # if len(key) < 7:
            # print("Cheia trebuie să aibă o lungime minimă de 7 caractere.")
            # continue

        text = input("Introduceți textul sau criptograma: ")

        if validate_input(text):
            result = vigenere_algorithm(text, key, operation)
            print(f"Rezultatul operației de {operation} este: {result}")
        
        next_move = input("Doriți să continuați (da/nu)? ").lower()
        if next_move != 'da':
            break

if __name__ == "__main__":
    main()
