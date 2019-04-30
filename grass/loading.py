
import csv
import numpy as np
def safe_float(number):
    try:
        return float(number)
    except:
        return None
def load_data(filename):
    csvFile = open(filename, 'r')
    reader = csv.reader(csvFile)

    data = []
    label = []
    for i in reader:
        if reader.line_num == 1:
            continue
        data.append(list(map(safe_float, i[:5])))
        if i[5] == "class1":
            label.append(0)
        if i[5] == "class2":
            label.append(1)
        if i[5] == "class3":
            label.append(2)
        if i[5] == "class4":
            label.append(3)
        if i[5] == "class5":
            label.append(4)
    return np.array(data),np.array(label)


if __name__ == "__main__":
    data,label = load_data()
    print(label)




