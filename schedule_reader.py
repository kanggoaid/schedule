import pandas as pd

Location = 'excel'
File = 'scadule.xlsx'

data_pd = pd.read_excel('{}/{}'.format(Location, File),
                     header=None, index_col=None, names=None)

#시간표 수작업이 귀찮지만 머리쓰기도 귀찮은 휘근쨩의 무지성무논리30분코딩 우효ww시간표리더기

#시간표 형식이 바뀌면 새로 만들던가 수정 필요
#무지성 코딩이라 다시 짜는게 편할 수도 있음

h=4
#행

y=1
#열

for i in range(0, 24):
    y=1
    E = (i%8) + 1
    #반

    M = (i//8) + 1
    #학년
    
    print('"' +str(M) + "-" + str(E)+ '" : [')

    for j in range(1, 13):
        if y>12:
            break

        else:
            if y==1:
                print('["' + data_pd.iloc[h, y] + '", ', end=' ')
                y = y + 1

            elif y==6:
                print('"' + data_pd.iloc[h, y] + '",], ', end=' ')
                y = y + 1

            elif y==7:
                print('["' + data_pd.iloc[h, y] + '", ', end=' ')
                y = y + 1

            elif y==12:
                print('"' + data_pd.iloc[h, y] + '",], ', end=' ')
                y = y + 1

            else:
                print('"'+data_pd.iloc[h,y]+'", ', end= ' ')
                y = y + 1

        if j==6:
            print(" ")

    print(" ")

    for j in range(1, 8):
        if y>19:
            break

        else:
            if y == 13:
                print('["' + data_pd.iloc[h, y] + '", ', end=' ')
                y = y + 1

            elif y == 19:
                print('"' + data_pd.iloc[h, y] + '",], ', end=' ')
                y = y + 1

            else:
                print('"' + data_pd.iloc[h, y] + '", ', end=' ')
                y = y + 1

        if j==7:
            print(" ")

    for j in range(1, 13):
        if y>31:
            break

        else:
            if y == 20:
                print('["' + data_pd.iloc[h, y] + '", ', end=' ')
                y = y + 1

            elif y == 25:
                print('"' + data_pd.iloc[h, y] + '",], ', end=' ')
                y = y + 1

            elif y == 26:
                print('["' + data_pd.iloc[h, y] + '", ', end=' ')
                y = y + 1

            elif y == 31:
                print('"' + data_pd.iloc[h, y] + '",] ', end=' ')
                y = y + 1

            else:
                print('"' + data_pd.iloc[h, y] + '", ', end=' ')
                y = y + 1

        if j==6:
            print("")
            
    print("\n],")
    h = h + 3
    

