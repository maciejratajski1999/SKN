import csv
import json

with open('22.csv') as csvfile:
    data = csv.reader(csvfile)
    data = [line for line in data]
    data = data[1:]
    # m = [line for line in data if line[2] == 'Mężyczyzna']
    # f = [line for line in data if line[2] == 'Kobieta']
    age_categories = ['Poniżej 15',
                      '15-18',
                      '19-22',
                      '23-26',
                      'Powyżej 26']
    data_by_age = [[line for line in data if line[1] == age] for age in age_categories]



    # for age in data_by_age:
    #     print(age)
# print(m)
# print(f)


def count_by_index(data, index):
    count = {}
    for line in data:
        if line[index]:
            if line[index] in count.keys():
                count[line[index]] += 1
            else:
                count[line[index]] = 1
    return count

data_sorted_by_age = {}
for age in data_by_age:
    nested_dict = {}
    for i in range(4, 14):
        if age:
            # print(f"{age[0][1]} {i}")
            # print(count_by_index(age, i))
            count = count_by_index(age, i)
            amount = sum([value for value in count.values()])
            count['razem'] = amount
            nested_dict['pytanie ' + str(i-3)] = count
    if age:
        data_sorted_by_age[age[0][1]] = nested_dict

with open('data_sorted_by_age.json', 'w') as jsonfile:
    json_string = json.dump(data_sorted_by_age, jsonfile, indent=4, sort_keys=False, ensure_ascii=False)

data_sorted_by_question = {}
for i in range(4, 14):
    nested_dict = {}
    for age in data_by_age:
        if age:
            count = count_by_index(age, i)
            amount = sum([value for value in count.values()])
            count['razem'] = amount
            nested_dict[age[0][1]] = count
    data_sorted_by_question['pytanie ' + str(i-3)] = nested_dict

with open('data_sorted_by_question.json', 'w') as jsonfile:
    json_string = json.dump(data_sorted_by_question, jsonfile, indent=4, sort_keys=False, ensure_ascii=False)
