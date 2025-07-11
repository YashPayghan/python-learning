alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def cipher(original_text,shift_amount):
    if direction == 'encode':
        def encrypt(original_text, shift_amount):
            global cipher_text
            cipher_text = ""
            for letter in original_text:
                shifted_position = alphabet.index(letter) + shift_amount
                if shifted_position >= len(alphabet):
                   shifted_position -= len(alphabet)
                cipher_text+= alphabet[shifted_position]
            print(f"Here is the encoded result: {cipher_text}")
        encrypt(original_text=text, shift_amount=shift)
    elif direction == 'decode':
        def decrypt(original_text, shift_amount):
            decipher_text = ""
            for letter in cipher_text:
                shifted_position = alphabet.index(letter) - shift_amount
                if shifted_position < 0:
                    shifted_position += len(alphabet)
                decipher_text += alphabet[shifted_position]
            print(f"Here is the decoded result: {decipher_text}")
        decrypt(original_text=text, shift_amount=shift)
    else:
        print("Invalid direction")
cipher(original_text=text,shift_amount=shift)
again=input("do you want to continue?(yes/no)\n")
if again == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    cipher(original_text=text,shift_amount=shift)
elif again == 'no':
    print("process finished")
else:
    print("invalid input")