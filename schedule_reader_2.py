import pandas as pd
import json

"""
1교시에 시작해서 2교시에 끝난 뭐같은 프로그램
"""

Location = 'excel'
File = 'schedule.xlsx'

data_pd = pd.read_excel(File, header=None, index_col=None, names=None)

jsonOut = {}

Magic = 0
while True:
    Magic += 1
    y = 19 * Magic - 18
    Class = ""
    try:
        Class = data_pd.iloc[y, 3]
    except:
        break
    #print(Class)

    yyyyy = []
    for i in range(5):
        i += 1
        #print(data_pd.iloc[(y + i + 1 + (i - 1) * 2), 0])
        x = 0
        xxxxx = []
        try:
            while True:
                x += 1
                shc = data_pd.iloc[(y + i + 1 + (i - 1) * 2), x]
                xxxxx.append(shc)
                #print(shc)
        except:
            yyyyy.append(xxxxx)
            continue
    jsonOut[Class] = yyyyy

with open("schedule.json", 'w') as outfile: 
    json.dump(jsonOut, outfile, indent=4, ensure_ascii=False)
