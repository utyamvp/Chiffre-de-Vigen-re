import os

def generate_key():
    # Генерация и возвращение ключа шифрования
    return input("Enter the encryption key: ")

def encrypt_text(text, key):
    # Шифрование текстового сообщения
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            # Преобразуем символы в верхний регистр для простоты
            char = char.upper()
            # Получаем номер буквы в алфавите (A=0, B=1, ..., Z=25)
            plain_text_char_index = ord(char) - ord('A')
            # Получаем номер буквы ключа
            key_char = key[i % key_length]
            key_char_index = ord(key_char.upper()) - ord('A')
            # Шифруем букву с помощью шифра Виженера
            encrypted_char_index = (plain_text_char_index + key_char_index) % 26
            # Преобразуем номер буквы обратно в символ
            encrypted_char = chr(encrypted_char_index + ord('A'))
            encrypted_text += encrypted_char
        else:
            # Оставляем все не-буквы без изменений
            encrypted_text += char
    return encrypted_text

def decrypt_text(encrypted_text, key):
    # Дешифрование текстового сообщения
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            # Преобразуем символы в верхний регистр для простоты
            char = char.upper()
            # Получаем номер буквы в алфавите (A=0, B=1, ..., Z=25)
            encrypted_char_index = ord(char) - ord('A')
            # Получаем номер буквы ключа
            key_char = key[i % key_length]
            key_char_index = ord(key_char.upper()) - ord('A')
            # Дешифруем букву с помощью шифра Виженера
            decrypted_char_index = (encrypted_char_index - key_char_index) % 26
            # Преобразуем номер буквы обратно в символ
            decrypted_char = chr(decrypted_char_index + ord('A'))
            decrypted_text += decrypted_char
        else:
            # Оставляем все не-буквы без изменений
            decrypted_text += char
    return decrypted_text

def encrypt_file(file_path, key):
    # Шифрование файла
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        plain_text = f.read()
    encrypted_text = encrypt_text(plain_text, key)
    encrypted_file_path = file_path + '.encrypted'
    with open(encrypted_file_path, 'w', encoding='utf-8') as f:
        f.write(encrypted_text)
    print(f"File content: {plain_text}")  # Выводим содержимое файла
    print(f"Encrypted text: {encrypted_text}\n")  # Зашифрованное содержимое файла

def decrypt_file(file_path, key):
    # Дешифрование файла
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        encrypted_text = f.read()
    decrypted_text = decrypt_text(encrypted_text, key)
    print(f"Decrypted text: {decrypted_text}\n")  # Дешифрованное содержимое файла

def process_files_in_directory(directory_path, key):
    # Шифрование и дешифрование всех файлов в директории
    for dirpath, _, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if filename.endswith(".txt"):
                encrypt_file(file_path, key)
            elif filename.endswith(".txt.encrypted"):
                decrypt_file(file_path, key)
    print(f"All txt files in directory {directory_path} processed")

def main():
    key = generate_key()
    while True:
        print("Choose an option:")
        print("1. Encrypt/Decrypt a text message")
        print("2. Encrypt/Decrypt a file")
        print("3. Encrypt/Decrypt files in a directory")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            text = input("Enter the text to encrypt: ")
            encrypted_text = encrypt_text(text, key)
            decrypted_text = decrypt_text(encrypted_text, key)
            print(f"Original text: {text}")
            print(f"Encrypted text: {encrypted_text}")
            print(f"Decrypted text: {decrypted_text}\n")
        elif choice == '2':
            file_path = input("Enter the file path to encrypt/decrypt: ")
            if file_path.endswith(".txt"):
                encrypt_file(file_path, key)
            elif file_path.endswith(".txt.encrypted"):
                decrypt_file(file_path, key)
            else:
                print("Invalid file type. Please provide a .txt or .txt.encrypted file.")
        elif choice == '3':
            directory_path = input("Enter the directory path: ")
            process_files_in_directory(directory_path, key)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
