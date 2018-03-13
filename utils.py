import re
import os

def blocks(files):  # useful function that counts blocks in a file
    while True:
        b = files.read(65536)  # reading file by blocks
        if not b: break
        yield b    # returning a generator, loads stuff into memory on the fly and gets iterated once

def lines(filename):
    with open(filename, "r") as f:
        return sum(block.count("\n") for block in blocks(f))

def times(filename, stuff):
    found = 0
    with open(filename, "r") as f:
        for block in blocks(f):
            found += len((re.findall(stuff, block)))
    return found

def charTimes(filename, char):
    if char == "":
        return os.stat(filename).st_size

    times(filename, char)

def wordTimes(filename, word):
    words = 0
    if word == "":
        with open(filename, "r") as f:
            for block in blocks(f):
                words += len(block.split(" "))
        return words

    times(filename, char)

def vfrequency(filename):
    pre = dict()
    per = dict()
    total = 0
    t   = ""
    with open(filename, "r") as f:
        t = f.read()

    matches    = re.findall(r'[a|e|i|o|u|y]', t)
    for match in matches:
        if match in pre:
            pre[match] += 1
        else:
            pre[match] = 1

    for m in pre.values():
        total += m

    for preppo in pre:
        per[preppo] = float("{:.2f}".format((100 * pre[preppo]) / total)) # % : 100 = p : T

    return per

def frequency(filename):
    pre = dict()
    per = dict()
    total = 0
    t   = ""
    with open(filename, "r") as f:
        t = f.read()

    matches = re.findall(r'[A-Za-z]', t)
    # print(len(matches))
    for match in matches:
        if match in pre:
            pre[match] += 1
        else:
            pre[match] = 1
    for m in pre.values():
        total += m

    for preppo in pre:
        per[preppo] = float("{:.2f}".format(100 * pre[preppo] / float(total))) # % : 100 = p : T
        # casting on total was necessary due to boh

    return per
