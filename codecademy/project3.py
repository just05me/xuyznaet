class Cipher:
    class CaesarCipher:
        def __init__(self, offset=0):
            self.offset = offset

        def encode(self, message):
            encoded_message = ""
            for char in message:
                if char.isalpha():
                    shift = ord('a') if char.islower() else ord('A')
                    encoded_message += chr((ord(char) - shift + self.offset) % 26 + shift)
                else:
                    encoded_message += char
            return encoded_message

        def decode(self, message):
            decoded_message = ""
            for char in message:
                if char.isalpha():
                    shift = ord('a') if char.islower() else ord('A')
                    decoded_message += chr((ord(char) - shift - self.offset) % 26 + shift)
                else:
                    decoded_message += char
            return decoded_message

        @staticmethod
        def brute_force_decode(message):
            for possible_offset in range(26):
                decoded_message = ""
                for char in message:
                    if char.isalpha():
                        shift = ord('a') if char.islower() else ord('A')
                        decoded_message += chr((ord(char) - shift - possible_offset) % 26 + shift)
                    else:
                        decoded_message += char
                print(f"Offset {possible_offset}: {decoded_message}\n")

    class VigenereCipher:
        def __init__(self, keyword):
            self.keyword = keyword

        def encode(self, message):
            encoded_message = []
            keyword_repeated = (self.keyword * (len(message) // len(self.keyword) + 1))[:len(message)]
            for i in range(len(message)):
                if message[i].isalpha():
                    shift = ord(keyword_repeated[i].lower()) - ord('a')
                    new_char = chr((ord(message[i].lower()) - ord('a') + shift) % 26 + ord('a'))
                    encoded_message.append(new_char.upper() if message[i].isupper() else new_char)
                else:
                    encoded_message.append(message[i])
            return ''.join(encoded_message)

        def decode(self, message):
            decoded_message = []
            keyword_repeated = (self.keyword * (len(message) // len(self.keyword) + 1))[:len(message)]
            for i in range(len(message)):
                if message[i].isalpha():
                    shift = ord(keyword_repeated[i].lower()) - ord('a')
                    new_char = chr((ord(message[i].lower()) - ord('a') - shift + 26) % 26 + ord('a'))
                    decoded_message.append(new_char.upper() if message[i].isupper() else new_char)
                else:
                    decoded_message.append(message[i])
            return ''.join(decoded_message)

caesar_cipher = Cipher.CaesarCipher(offset=10)
encoded_message = "xuo jxuhu! jyxi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiuqwu rqsa myjx jxu iqcu evviuj!"
decoded_message = caesar_cipher.decode(encoded_message)
print("Decoded Caesar Message:", decoded_message)

response_message = "This is my response to your encoded message!"
encoded_response = caesar_cipher.encode(response_message)
print("Encoded Caesar Response:", encoded_response)

unknown_shift_message = "vhfinmxkl atox kxgwxkw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzwl ltyx."
Cipher.CaesarCipher.brute_force_decode(unknown_shift_message)

vigenere_cipher = Cipher.VigenereCipher(keyword="friends")
encoded_vigenere_message = vigenere_cipher.encode("barry is the spy")
print("Encoded Vigenère Message:", encoded_vigenere_message)

decoded_vigenere_message = vigenere_cipher.decode("txm srom vkda gl lzlgzr qpdb?")
print("Decoded Vigenère Message:", decoded_vigenere_message)