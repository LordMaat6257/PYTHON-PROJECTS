alphabet = [chr(i) for i in range(97, 123)]
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"Here is the encoded result: {cipher_text}")
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift_amount) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += letter
    print(f"Here is the decoded result: {plain_text}")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print("Invalid choice. Please type 'encode' or 'decode'.")
