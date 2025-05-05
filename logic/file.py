import csv

class DataReader:
    def read_data(path: str, key_list: list, mapper: callable):
        data = []
        with open(path, mode='r', encoding='utf-8') as file:
            input = csv.DictReader(file)
            for row in input:
                filtered_row = {key: row[key] for key in key_list if key in row}
                data.append(mapper(**filtered_row))
        return data