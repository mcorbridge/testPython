from Crypto.Cipher import AES
from Crypto.Util import Padding
from hashlib import md5
from base64 import b64encode, b64decode

# from --> https://gist.github.com/Frizz925/ac0fb026314807959db5685ac149ed67  Izra Faturrahman
# unbreakable except from Rubber-hose cryptanalysis

class TestingCrypto:

    def __init__(self):
        print("Testing Crypto")

        self.passphrase = "Wally"
        self.content = ""
        self.mode = AES.MODE_CBC
        self.bs = AES.block_size
        self.result = ""

    def encrypt(self, plaintext):
        print("encrypt this plaintext: " + plaintext)
        self.content = plaintext
        key = md5(self.passphrase.encode('utf-8')).hexdigest().encode('utf-8')
        body = Padding.pad(self.content.encode('utf-8'), self.bs)
        iv = key[8:self.bs + 8]
        cipher = AES.new(key, self.mode, iv)
        key = b64encode(key).decode('utf-8')
        body = b64encode(cipher.encrypt(body)).decode('utf-8')
        iv = b64encode(iv).decode('utf-8')
        self.result = "%s.%s.%s" % (key, body, iv)
        print("encrypted text:")
        print(self.result)

    def decrypt(self, encryptedData, passphrase):
        print("decrypt :")
        try:
            key, body, iv = encryptedData.split(".")
            key = md5(passphrase.encode('utf-8')).hexdigest().encode('utf-8')
            body = b64decode(body.encode('utf-8'))
            iv = b64decode(iv.encode('utf-8'))
            cipher = AES.new(key, self.mode, iv)
            body = Padding.unpad(cipher.decrypt(body), self.bs).decode('utf-8')
            print(body)
        except ValueError:
            print("WRONG PASSWORD! Nice try asshole!")


plaintext = "Beto O'Rourke's best moment on Thursday's Democratic presidential debate -- which also doubled as his best" \
"moment in the 2020 campaign to date -- came when ABC's David Muir asked whether he supported a mandatory " \
"buyback of assault weapons. Hell, yes, we're going to take your AR-15, your AK-47, O'Rourke said to raucous " \
"applause from the crowd in Houston, Texas. We're not going to allow it to be used against our fellow"\
"Americans anymore."

testingCrypto = TestingCrypto()
testingCrypto.encrypt(plaintext)

encryptedData = "ODc4OWI0NWRlMzI4MDFhZDIyMGY1OWU2NmQyOWYzZTk=.hf3dzkSVEXPTMysfox+maP7S7Qj/dTfOcP2bKOGPnQGw/L6JaK+0nMTAs"\
"R9dfZGcUUtL/D+mgAnB+Q8ZKRFcCUorCmyhbo3BT5q8Wkt6d+pgqQYuzz0ECx9jAiI3K/VvlD3zYlOc1G0WHbVP1JtJqSu5ZwB7tibkdm578oDbEIx/fBMq"\
"2enoe36l+WmbGvBkNr8lMCwj3M1snezCE4hrPQPRC8sU/Ld1ZbxlJ+r29r18y2m2JO37lcrUKAu3zH5oIrTDTvm1OK4UX2qhMyzu/2Quj2tZ/6vwLpZzW5M"\
"WTDLBUU69r+E1L8EUAWdEtqb/4aM3CdKT5Ls6O7WePww68N4ZXUxRUun3QJ6RBMqTVyeKvS2cfXGI18ce8pDNGbcVTTnqOZUjh7JhjDqfFF62Phc8zjCmoV"\
"j2/vYiVVOEeMdMWUSeOh0TclFiCsNREZJ/EMDyWn8v4ZdHoiRxlgqsgj0gQQuCzTUKCaHy73uWWdluZ7s+U3lZ8qXkiBPdkSZZAikMprChQypfSE2dI1Hfl"\
"vRrJaqAwMf316FYklDaWEUQi5sfPvCEwpdtYEs4/hfzwgoZLQ9rxdErMjUCN548Ag==.ZTMyODAxYWQyMjBmNTllNg=="

testingCrypto.decrypt(encryptedData, "Wally")


