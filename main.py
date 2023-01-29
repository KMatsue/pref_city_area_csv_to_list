import csv

city = ['指定なし']
stateCityItems = {}
city_name = ''
key_name = ''
csv_path = './area.csv'

with open(csv_path) as f:
    reader = csv.reader(f)
    # csvファイルのデータをループ
    for row in reader:

        if city_name != row[2]:
            city_name = str(row[2])
            # A列を配列へ格納
            if row[1] == key_name:
                city.append(str(row[2]))
                # stateCityItems[key_name] = city
            if row[1] != key_name:
                key_name = str(row[1])
                city = ['指定なし']
                list(set(city))
                stateCityItems[key_name] = city

if __name__ == '__main__':
    print(stateCityItems)
