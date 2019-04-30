
import csv
import numpy as np



def loading_data():
    csvfile = open('../1.csv','r')
    reader = csv.reader(csvfile)
    data = []
    for i in reader:
        if reader.line_num == 1:
            continue
        data.append(list(i[:6]))
    return data


def splits_data(data):
    class1 = []
    class2 = []
    class3 = []
    class4 = []
    class5 = []
    for i in data:
        if i[5] == "class1":
            class1.append(i)
        if i[5] == "class2":
            class2.append(i)
        if i[5] == "class3":
            class3.append(i)
        if i[5] == "class4":
            class4.append(i)
        if i[5] == "class5":
            class5.append(i)
    return class1,class2,class3,class4,class5


def save_data(class1,class2,class3,class4,class5):
    train = []
    test = []
    for i in range(len(class1)):
        if i < 200 :
            test.append(class1[i])
        else:
            train.append(class1[i])

    for i in range(len(class2)):
        if i < 200 :
            test.append(class2[i])
        else:
            train.append(class2[i])

    for i in range(len(class3)):
        if i < 200 :
            test.append(class3[i])
        else:
            train.append(class3[i])

    for i in range(len(class4)):
        if i < 200 :
            test.append(class4[i])
        else:
            train.append(class4[i])

    for i in range(len(class5)):
        if i < 200 :
            test.append(class5[i])
        else:
            train.append(class5[i])
    return train,test
def save_csv(train,test):
    with open("../train.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        # 先写入columns_name
        writer.writerow(["tbdgd","ksmcbl","thzszbl","tryjzhl","shqk","class"])
        # 写入多行用writerows
        writer.writerows(train)
        csvfile.close()

    with open("../test.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        # 先写入columns_name
        writer.writerow(["tbdgd","ksmcbl","thzszbl","tryjzhl","shqk","class"])
        # 写入多行用writerows
        writer.writerows(test)
        csvfile.close()




if __name__ == "__main__":
    data = loading_data()
    print(data)
    class1, class2, class3, class4, class5 = splits_data(data)
    train,test = save_data(class1, class2, class3, class4, class5)
    save_csv(train,test)