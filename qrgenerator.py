import glob
import qrcode

files = glob.glob("configs/*/rehid.json")
testfiles = glob.glob("testconfigs/*/rehid.json")

i = 0
for file in files:
    with open(file, "r") as f:
        data = f.read()
        img = qrcode.make(data)
        loc = file[file.find("/") + 1:]
        loc = loc[:loc.find("/")]
        img.save("configs/" + loc + "/qr.png")
        f.close()
        i = i + 1

i = 0
for file in testfiles:
    with open(file, "r") as f:
        data = f.read()
        img = qrcode.make(data)
        loc = file[file.find("/") + 1:]
        loc = loc[:loc.find("/")]
        img.save("testconfigs/" + loc + "/qr.png")
        f.close()
        i = i + 1