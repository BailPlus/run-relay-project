import json,os

for i in os.listdir('raw'):
    latlons = []
    with open(os.path.join('raw',i)) as file:
        try:
            data = json.load(file)['data']
        except json.decoder.JSONDecodeError as e:
            raise ValueError(f'处理{i}文件有误') from e
    for j in data:
        latlons.append((j['latitude'],j['longitude']))
    with open(os.path.join('latlons',i),'w') as file:
        json.dump(latlons,file)
