alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(text,shift):
    next=""
    for letter in text:
       that_shift= alphabet.index(letter)+shift
       if that_shift > len(alphabet):
             that_shift-=len(alphabet)

       next+=alphabet[that_shift]
    print("encrypted_text is",next)
encrypt(text,shift)