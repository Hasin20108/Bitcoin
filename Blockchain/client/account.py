import sys
sys.path.append('C:/Users/mdhsn/OneDrive/Desktop/Bitcoin')
# sys.path.append('c:/Users/Has/Desktop/Academic/Project/Bitcoin')

from Blockchain.Backend.core.database.database import AccountDB
from Blockchain.Backend.core.EllepticCurve.EllepticCurve import Sha256Point
from Blockchain.Backend.util.util import hash160, hash256
import secrets
BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

class Account:
    def createKeys(self):
        Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
        Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

        G = Sha256Point(Gx, Gy)

        self.privateKey = secrets.randbits(256)

        unCompressedPublicKey = self.privateKey * G
        xpoint = unCompressedPublicKey.x
        ypoint = unCompressedPublicKey.y

        # print(f"type of xpoint and ypoint = {type(Xpoint.num)}, {type(Ypoint)}")

        # print(f"Private Key is {privateKey}")
        # print(f"unCompressedPublicKey = {unCompressedPublicKey}")

        if ypoint.num % 2 == 0:
            compressKey = b'\x02' + xpoint.num.to_bytes(32, 'big')
        else:
            compressKey = b'\x03' + xpoint.num.to_bytes(32, 'big')

        hsh160 = hash160(compressKey)

        """Prefix for Mainnet"""
        main_prefix = b'\x00'

        newAddr = main_prefix + hsh160

        # print(f"hsh160 = {hsh160}")
        # print(f"hsh160(integer) = {int.from_bytes(hsh160)}")
        # print(f"hsh160(hex) = {hex(int.from_bytes(hsh160))}")
        
        # print(f"data type of compresskey= {type(compressKey)}")        
        # print(f"compressKey = {compressKey}")        
        # print(f"data type of newAddr = {type(newAddr)}")        
        # print(f"newAddr = {newAddr}")

        checksum = hash256(newAddr)[:4]
        # print(newAddr)
        newAddr = newAddr + checksum
        # print(checksum)
        # print(newAddr)

        # print(f"\n\n newAddr = {newAddr}")
        # print(f"newAddr(integer) = {int.from_bytes(newAddr)}")
        # print(f"newAddr(hex) = {hex(int.from_bytes(newAddr))} \n\n")
        
        count = 0

        for c in newAddr:
            if c == 0:
                count += 1
            else:
                break

        prefix = '1' * count

        result = ''

        num = int.from_bytes(newAddr, 'big')
        
        # print(f"newAddr (bytes) = {newAddr}")
        # print(f"newAddr (integer) = {num}")
        
        while num > 0:
            num, mod = divmod(num, 58)
            result = BASE58_ALPHABET[mod] + result
        
        self.PublicAddress = prefix + result
        
        print(f"private Key = {self.privateKey}")
        print(f"public Key = {self.PublicAddress}")

if __name__ == '__main__':
    account = Account()
    account.createKeys()
    AccountDB().write([account.__dict__])