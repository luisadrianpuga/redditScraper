import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()

text_file = open("main.txt", "r")
lines = text_file.readlines()
print(lines)
print(len(lines))
text_file.close()

converted_list = []

for element in lines:
    converted_list.append(element.strip())

print(len(converted_list))

converted_list = set(converted_list)
print(len(converted_list))

converted_list = list(converted_list)
print(len(converted_list))
i=0
with open("cleanedKeyWords.txt", "w") as output:
    for item in converted_list:
  
        
        output.write(str(converted_list[i])+ '\n')
        i+=1