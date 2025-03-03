import string

def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift  # Reverse the shift for decryption

    alphabet = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]  
    table = str.maketrans(alphabet, shifted_alphabet)  

    return text.translate(table)

# User Input
choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()
message = input("Enter your message: ")
shift = int(input("Enter shift key (1-25): "))

if choice == 'e':
    result = caesar_cipher(message, shift)
    print("🔒 Encrypted Message:", result)
elif choice == 'd':
    result = caesar_cipher(message, shift, decrypt=True)
    print("🔓 Decrypted Message:", result)
else:
    print("Invalid choice. Please select 'E' or 'D'.")
