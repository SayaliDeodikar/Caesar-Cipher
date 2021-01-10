alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
print(art.logo)

def caesar(message, position, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            position *= -1
    for char in message:
        if char in alphabet:
            original = alphabet.index(char)
            new = original + position
            end_text += alphabet[new]
        else:
            end_text += char
    print(f"The {cipher_direction}d is {end_text}")

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift %= 26
  caesar(text, shift, direction)
  choice = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
  if choice == 'no':
    should_continue = False
    print("Goodbye!")