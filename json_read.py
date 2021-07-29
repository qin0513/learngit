import json

def json_f_read(file_name):
    with open(file_name,'r',encoding='utf-8') as f:
        danmu_dic = json.load(f)
    return danmu_dic
danmu_dic_1 = json_f_read("av号1Xv411E7qr.json")
danmu_dic_2 = json_f_read("av号90748215.json")
def read_danmu(danmu_dic):
    danmu_list = []
    for key, value in danmu_dic.items():
        if type(value) == list:
            danmu_list.append(value)
    return danmu_list
danmu_list_1 = read_danmu(danmu_dic_1)
danmu_list_2 = read_danmu(danmu_dic_2)

count = 0
for i in range(len(danmu_dic_1)):
    list_dan_1 = danmu_list_1[0]
    list_dan_2 = danmu_list_2[0]
    if list_dan_1[1] != list_dan_2[1]:
        count += 1

if count > 0:
    print("文件不相同")