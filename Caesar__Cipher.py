alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encode():
    text = input("Enter message to encode  : ").lower()
    shift = int(input("Enter Shift : "))
    encode=""
    for i in text:
        text_index = alphabets.index(i)
        shift_word = text_index + shift
        if shift_word >=26:
          over_length = shift_word - 26
          encode+=alphabets[over_length]
        else:
          shift_word = text_index + shift
          encode+=alphabets[shift_word]
    print(' '.join(encode))#to join ' ' space with letters in encode

def decode():
    text1 = input("Enter message to decode  : ").lower()
    shift1 = int(input("Enter Shift  : "))
    decode=""
    for i in text1:
        text_index1 = alphabets.index(i)
        shift_word1 = text_index1 - shift1
        decode+=alphabets[shift_word1]
    print(f"{' '.join(decode)}")
while True:
  print("\n\n\t\tCaesar Cipher\n")
  option = input("Type 'encode' to encrypt, type 'decode' to decrypt or 'exit': ").lower()
  if option == 'encode':
    encode()
  elif option == 'decode':
    decode()
  elif (option != 'exit') & (option != 'decode') & (option != 'encode'):
    print("\t___INVALID___")
  elif option == 'exit':
    break
  