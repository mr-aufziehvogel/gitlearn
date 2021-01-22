
import subprocess

letters = "abcdefghijklmnopqrstuvwxyz0123456789"

# for i in letters:
#     for j in letters:
for k in letters:
    for l in letters:
        numchar = k + l
        proc = subprocess.Popen(['python3', './hack.cpython-38.pyc', '--t', numchar], stdout=subprocess.PIPE, universal_newlines=True)
        output = proc.stdout.read().strip()
        print(numchar)
        if output != "Nope":
            print ("XXXXXXXXXXXXXXXXXXXXXXX")
