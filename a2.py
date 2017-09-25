""" William Guntur Compsci 220 Assignment 2
"Songsort" - Sorting songs based on runtime and title
through merge sort """

from operator import itemgetter
import sys

# Python recursive implementation of merge sort

def mergesort(x):
        if len(x)>1:
                m = len(x) // 2
                l = x[:m]
                r = x[m:]
                mergesort(l)
                mergesort(r)
                i = 0
                j = 0
                k = 0
                while i < len(l) and j < len(r):
                        if l[i][0] > r[j][0]:
                                x[k] = l[i]
                                i += 1                        
                        elif l[i][0] == r[j][0]:
                                if l[i][1] < r[j][1]:
                                        x[k] = l[i]
                                        i += 1
                                elif l[i][1] == r[j][1]:
                                        if l[i][2] < r[j][2]:
                                                x[k] = l[i]
                                                i += 1
                                        else:
                                                x[k] = r[j]
                                                j += 1
                                else:
                                        x[k] = r[j]
                                        j += 1 
                        else:
                                x[k] = r[j]
                                j += 1
                        k += 1
                     
                while i < len(l):
                        x[k] = l[i]
                        i += 1
                        k += 1
                while j < len(r):
                        x[k] = r[j]
                        j += 1
                        k += 1

# Taking input
songs = []
songs_tuples = []
for line in sys.stdin:
        songs.append(line)

k = int(songs.pop(0))
seperator = (songs.pop(0)).rstrip()
for song1 in songs:
        temp = song1.split(seperator)
        #print(temp)
        songs_tuples.append((int(temp[2]), temp[0], temp[1], song1))


mergesort(songs_tuples)
newlist = []
for line1 in songs_tuples:
        if k > 0:
                sys.stdout.write(line1[3] + "\n")
                k -=1



