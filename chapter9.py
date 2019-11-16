import os
os.path.join("download", "self_learning_of_python", "chapter9.txt")
#1 コメントアウトをとると実行可能
#chapter9 = open("chapter9.txt", "w")
#chapter9.write("Rit is always thinking.")
#chapter9.close()

#2　コメントアウトをとると実行可能
#chapter9 = open("chapter9.txt", "w")
#ans = input ("what to write?")
#chapter9.write(ans)
#chapter9.close()

#3
import csv
with open ("chapter9.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow([["a","b","c"],["d","e","f"],["g","h","i"]])
