import os
import json
#获取目标文件夹的路径
filedir = 'each_rail_transit_information'
#获取文件夹中的文件名称列表（含文件扩展名）
filenames = os.listdir(filedir)
pass
all_buslines = []
for filename in filenames:
    # 每个文件的路径（这里为方便，取相对路径）
    filePath = filedir + '\\' + filename
    # 文件对象
    file = open(filePath, "rb")
    # 加载json文件的内容
    jsonContents = json.load(file)
    for jsonContent in jsonContents:
        bus_line = []
        tempRailStationsGPS = []
        railStationsGPS = jsonContent['railStations']['railStationsGPS']
        n = len(railStationsGPS) # n为双数（这是显然的）
        for i in range(0, n, 2):
            tempRailStationsGPS.append([railStationsGPS[i], railStationsGPS[i+1]])
        bus_line.append({'railLineName': jsonContent['raillineName']})
        for railStationName, railStationGPS in zip(jsonContent['railStations']['railStationsName'], tempRailStationsGPS):
            bus_line.append({'railStationName': railStationName, 'railStationGPS': railStationGPS})
        all_buslines.append(bus_line)
pass
jsonData = json.dumps(all_buslines, indent=2, ensure_ascii=False)
jsonFile = open('all_rail_transit_station_information_1.json', 'w', encoding='utf-8')
jsonFile.write(jsonData)
jsonFile.close()
print(len(all_buslines))
