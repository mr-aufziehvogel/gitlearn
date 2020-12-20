import argparse
import random
import string

parser = argparse.ArgumentParser(description='Good luck')
parser.add_argument("--t", default=1, help="Your guess")

random.seed(16)
number = random.randint(1,99)

letter = (random.choice(string.ascii_letters.lower()))
letter2 = (random.choice(string.ascii_letters.lower()))

pw = letter + str(number) + letter2
# print(pw)

args = parser.parse_args()
t = args.t
if t == str(pw):
    print("You did it!")
else:
    print("Nope")