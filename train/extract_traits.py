import json,os,pandas as pd
from math import radians, sin, cos, sqrt, atan2

def haversine(lon1, lat1, lon2, lat2):
    """
    计算两个点之间的地球表面距离（单位：米）
    """
    lon1, lat1, lon2, lat2 = map(radians, [float(lon1), float(lat1), float(lon2), float(lat2)])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = atan2(2 * sqrt(a),sqrt(1-a))
    r = 6371000 # 地球半径, 单位：米
    return c * r

def calculate_features(points):
    distances = []
    directions = []
    prev_point = None
    
    for point in points:
        if prev_point:
            distance = haversine(prev_point[1], prev_point[0], point[1], point[0])
            distances.append(distance)
            
            # 方向变化计算
            dx = float(point[1]) - float(prev_point[1])
            dy = float(point[0]) - float(prev_point[0])
            direction = atan2(dy, dx)
            directions.append(direction)
            
        prev_point = point
    
    total_distance = sum(distances)
    avg_speed = total_distance / (len(points) - 1) if len(points) > 1 else 0
    dir_change_std = (pd.Series(directions).std() if len(directions) > 1 else 0) if directions else 0
    
    return total_distance, avg_speed, dir_change_std

if __name__ == '__main__':
    for i in os.listdir('latlons'):
        with open(os.path.join('latlons',i)) as file:
            data = json.load(file)
        result = calculate_features(data)
        with open(os.path.join('traits',i),'w') as file:
            json.dump(result,file)
