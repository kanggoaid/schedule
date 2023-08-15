import pandas as pd
import json

"""
1교시에 시작해서 2교시에 끝난 뭐같은 프로그램
아마 대체로 맞는듯..?
"""

Location = 'excel'
File = 'schedule.xlsx'

data_pd = pd.read_excel(File, header=None, index_col=None, names=None)

jsonOut = {}

for y in range(4, 51, 2):
    ClassJson = []
    for i in range(5):
        c = []
        for x in range(6):
            c.append(data_pd.iloc[y, 6 * i + x + 1])
        ClassJson.append(c)
    jsonOut[data_pd.iloc[y, 0]] = ClassJson

with open("schedule.json", 'w') as outfile: 
    json.dump(jsonOut, outfile, indent=4, ensure_ascii=False)
