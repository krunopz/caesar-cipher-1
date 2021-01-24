alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']                                                                  
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
text.split()
def encrypt(text,shift):
  encrypted_text=""
  for n in text:
      i=(alphabet.index(n)+shift)%len(alphabet)
      encrypted_text=encrypted_text+alphabet[i]

  print(f"The encoded text is: {encrypted_text}")


def decrypt(text,shift):
  decrypted_text=""
  for n in text:
    i=(alphabet.index(n)-shift)%len(alphabet)
    decrypted_text=decrypted_text+alphabet[i]

  print(f"The decoded text is: {decrypted_text}")

if direction=="encode":
  encrypt(text,shift)
elif direction=="decode":
  decrypt(text,shift)



    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
