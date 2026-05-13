import os.path
import glob
from cryptography.fernet import Fernet
from cryptography.fernet import binascii

home_dir=os.path.expanduser('~')
e_path = home_dir+"\\creds\**\*.*"

files = glob.glob(f"{e_path}", recursive=True)

# with open("ekey.key", "r") as kf:
#     ekey = kf.read()

ekey = input("Input the decryption key: ")

try:
    ofernet = Fernet(ekey)
except binascii.Error:
    print("incorrect key format!")
    exit()
for f in files:
    try:
        with open(f, 'rb') as Tfile_encrypted:
            Tfile_encrypted_bytes = Tfile_encrypted.read()
    except:
        pass
    try:
        decrpted_bytes = ofernet.decrypt(Tfile_encrypted_bytes)
        try:
            with open(f, 'wb') as Tfile_decrypting:
                Tfile_decrypting.write(decrpted_bytes)
                print("Decrypted", f, "Successfully!")
        except:
            print("somethings went wrong!")
            pass
    except:
        print("Wrong Decryption key!")
        pass
    # print("Decrypted", f, "successfully!")
# print("Recursively Decrypted all files Successfully!")