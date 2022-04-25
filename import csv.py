import csv
with open('次數.csv', newline='', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')    
    for row in rows:
        n = row[0]
        print(n)

#執行 5次後停止執行
if int(n) < 6:

#執行所需的程式片段(例如爬蟲)
    number_list = []
    for i in range(1,1000000*int(n)):
        number_list.append(i)
    print(number_list)   

#執行完將計數寫回CSV檔案
    with open('次數.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow([str(int(n)+101)[1:]])