from Crypto.Cipher import AES
from Crypto.Util import Padding
from hashlib import md5
from base64 import b64encode, b64decode

# from --> https://gist.github.com/Frizz925/ac0fb026314807959db5685ac149ed67

class TestingCrypto:

    def __init__(self):
        print("Testing Crypto")

        self.passphrase = "foo"
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

    def decrypt(self,encryptedData, passphrase):
        print("decrypt :")
        try:
            key, body, iv = encryptedData.split(".")
            key = md5(passphrase.encode('utf-8')).hexdigest().encode('utf-8')
            # key = b64decode(key.encode('utf-8'))
            body = b64decode(body.encode('utf-8'))
            iv = b64decode(iv.encode('utf-8'))
            cipher = AES.new(key, self.mode, iv)
            body = Padding.unpad(cipher.decrypt(body), self.bs).decode('utf-8')
            print(body)
        except:
            print("WRONG PASSWORD! Nice try asshole!")

plaintext = "Beto O'Rourke's best moment on Thursday's Democratic presidential debate -- which also doubled as his best"\
"moment in the 2020 campaign to date -- came when ABC's David Muir asked whether he supported a mandatory buyback of"\
"assault weapons. Hell, yes, we're going to take your AR-15, your AK-47, O'Rourke said to raucous applause from the"\
"crowd in Houston, Texas. We're not going to allow it to be used against our fellow Americans anymore."

testingCrypto = TestingCrypto()
testingCrypto.encrypt(plaintext)
encryptedData = "YWNiZDE4ZGI0Y2MyZjg1Y2VkZWY2NTRmY2NjNGE0ZDg=.xMcPOvog0HsV+4CxbmD2tjSGn+AhnQ6JJVN7rbDtEHUEmfP8ROFcYPY3"\
"okA7zaMsoLXKOU2RbfwQRzWzIBuVZ4i39/f6X8MmE9cP7EeJ1Aq6rZdLCdwQkErR2a4hPHv7r+VEdTOdOlS2vP+dYddK/Vj+qW7SYb3mDAtnP8fnK"\
"jw5M/Wx6au78coT0thEJI6xPE91tOT2NXsF9D4eWs5g1it8gX5adcIy4XG2zIvnXC65QlQIWdGQ/ueDsPH9/4vJsugkqKhr1ZFykz3IKi63i9v8+Bb8zwr1+md"\
"FvE06ZmEDLFxZ0yiSub2lvutAicIMPB2ul78y+CqETbVQ0sN8+jNfYxOz+LHrms+5gGw6DPWDihT3sD+tYidENTVNyFzeZVe6gyICAqxsfcDOlsIzWXkVmvgly"\
"IdguFZLdd+dtJxdyqHkNlpauvV1lUQfuoPBWTk+dNHv413TPwCf3MIdrrCmAR7rGOaMkRTamn/4IM7vLLPNXU413vuAFw9RqRUMb87EnO9K0"\
"gow11mNy29JSNuA1Tj9oPiCwzn0Fv/fzh8NARX4fZh8xd2qqRhmN26qSQyRxlTsBm1IT80pbjk4Yw==.NGNjMmY4NWNlZGVmNjU0Zg=="
testingCrypto.decrypt(encryptedData,"foo")
