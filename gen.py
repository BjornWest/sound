import math

import numpy
import scipy
from scipy.io import wavfile

samplerate, data = wavfile.read('C:/Users/bpfwe/Downloads/astly.wav')

print(samplerate)


def output(info, n, d):
    hz = 0
    for x in range(n):
        if numpy.sign(info[x][0]) != numpy.sign(info[x + 1][0]):
            hz += 1
        print(info[d * x][0], ",", end=' ')
    print()
    print(n * d / samplerate)
    print(hz)


def getMax(info):
    length = len(info)
    compareMax = 0
    for x in range(length):
        if abs(info[x][0]) > compareMax:
            compareMax = info[x][0]
    return compareMax


def FooRier(info, n):
    compareMax = getMax(info)
    print(compareMax)
    length = len(info)
    amplitudes = []
    for y in range(n):
        sum = 0
        for x in range(int(length / 100)):
            if math.sin(y * math.pi * x * 100 / length) != 0:
                sum += (info[x * 100][0] / (float(compareMax))) / math.sin(y * math.pi * x * 100 / length)
        amplitudes.append(sum / length * 100)
        print(y)
    print(amplitudes)
    return (amplitudes)


def compare(amplitudes, data, scale):
    for x in range(len(data)):
        compareSum = 0
        for y in amplitudes:
            compareSum += y * math.sin(y * math.pi * x / len(data))
        print(compareSum, data[x][0] / scale)


# a = FooRier(data,100)


wordList = []

def print_tree(lst):
    if len(lst) == 2:
        #print(f'pair({lst[0]},{lst[1]})', end="")
        wordList.append(f'pair({lst[0]},{lst[1]})')
    else:
        split = math.floor(len(lst) / 2)
        first = lst[:split]
        second = lst[split:]
        #print("pair(", end="")
        wordList.append("pair(")
        print_tree(first)
        #print(",", end="")
        wordList.append(",")
        print_tree(second)
        #print(")", end="")
        wordList.append(")")



def fill_list(lst):
    while math.log2(len(lst)) % 1 != 0:
        lst.append(0)
    return lst

def create_square(n):
    print("list(",end="")
    for a in range(n):
        print("list(",end="")
        for c in range(n):
            print(f'{a*n+c},',end="")
        print(")",end="")
    print(")", end="")

create_square(16)




b = []


size = 2**18
factor = 1/getMax(data)
print(getMax(data))
average = 10
for x in range(math.floor(size)):
    sum = 0
    for y in range(average):
        3#sum += data[x*average+y][0]/average
    b.append(round(data[40000+x*2][0]*factor,2))

print_tree(b)
with open('sound.txt', 'w') as f:
    for x in range(len(wordList)):
        if x % 100 == 0:
            f.write("\n")
        f.write(wordList[x])

for x in b:
    3#print(x,",",end="")


print(len(wordList))
# output(data,int(44100*5),10)
