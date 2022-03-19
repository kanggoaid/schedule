import pandas as pd

Location = 'excel'
File = 'schedule.xlsx'

data_pd = pd.read_excel('{}/{}'.format(Location, File),
                        header=None, index_col=None, names=None)

# 시간표 수작업도 싫고 머리쓰기도 귀찮은 휘근쨩의 무지성무논리30분코딩 시간표리더기
# 2022 1학기 시간표 기준
# 그냥 다시 만들자 tlqkf ㅋㅋ 하나하나 바꾸기 매우 귀찮음

h = 4
# 행

y = 1
# 열

for i in range(0, 24):
    y = 1
    E = (i % 8) + 1
    # 반

    M = (i // 8) + 1
    # 학년

    print('"' + str(M) + "-" + str(E) + '" : [')

    for j in range(1, 15):
        if y > 14:
            break

        else:
            if y == 1:
                print('["' + data_pd.iloc[h, y] + '", ', end=' ')
                y = y + 1

            elif y == 7:
                print('"' + data_pd.iloc[h, y] + '",], ', end=' ')
                y = y + 1

            elif y == 8:
                print('["' + data_pd.iloc[h, y] + '", ', end=' ')
                y = y + 1

            elif y == 14:
                print('"' + data_pd.iloc[h, y] + '",], ', end=' ')
                y = y + 1

            else:
                print('"' + data_pd.iloc[h, y] + '", ', end=' ')
                y = y + 1

        if j == 7:
            print(" ")

    print(" ")

    for j in range(1, 7):
        if y > 20:
            break

        else:
            if y == 15:
                print('["' + data_pd.iloc[h, y] + '", ', end=' ')
                y = y + 1

            elif y == 20:
                print('"' + data_pd.iloc[h, y] + '",], ', end=' ')
                y = y + 1

            else:
                print('"' + data_pd.iloc[h, y] + '", ', end=' ')
                y = y + 1

        if j == 6:
            print(" ")

    for j in range(1, 15):
        if y > 34:
            break

        else:
            if y == 21:
                print('["' + data_pd.iloc[h, y] + '", ', end=' ')
                y = y + 1

            elif y == 27:
                print('"' + data_pd.iloc[h, y] + '",], ', end=' ')
                y = y + 1

            elif y == 28:
                print('["' + data_pd.iloc[h, y] + '", ', end=' ')
                y = y + 1

            elif y == 34:
                print('"' + data_pd.iloc[h, y] + '",] ', end=' ')
                y = y + 1

            else:
                print('"' + data_pd.iloc[h, y] + '", ', end=' ')
                y = y + 1

        if j == 7:
            print("")

    print("\n],")
    h = h + 2
