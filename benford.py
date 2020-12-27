#!/usr/bin/env python
# coding: utf-8
import csv
import numpy as np
import matplotlib.pyplot as plt

benford_law = {1: 30.1, 2: 17.6, 3: 12.5, 4: 9.7, 5: 7.9, 6: 6.7, 7: 5.8, 8: 5.1, 9: 4.6}


def read_csv(path):
    # devolve lista tirada do csv
    all_values = []
    data = open(path, encoding="utf-8")
    csv_data = csv.reader(data)

    for num in csv_data:
        all_values.extend(num)
    return all_values


def get_first_digit(values_list):
    # devolve lista dos primeiros digitos da lista
    first_digits = []
    for num in values_list:
        # print(num)
        # print(int(str(num)[0]))
        # print("---")
        first_digits.append(int(str(num)[0]))

    return first_digits


def assign_first_digits(digits_list):
    # devolve dicionario c occorencia de cada digito
    amount_first_digits = {}

    for i in range(1, 10):
        amount_first_digits[i] = digits_list.count(i)

    return amount_first_digits


def digits_percentage(digits_dic, lengt):
    # devolve dicionario c a percentagem de occorencia de cada digito
    first_digits_percentage = {}

    for i in range(1, 10):
        first_digits_percentage[i] = (float(digits_dic[i]) / lengt) * 100

    return first_digits_percentage


def show_graphs(dic, ben):
    # mostra os dois graficos
    n = 19
    data_means = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, dic[1], dic[2], dic[3], dic[4], dic[5], dic[6], dic[7], dic[8], dic[9])
    benford_means = \
        (ben[1], ben[2], ben[3], ben[4], ben[5], ben[6], ben[7], ben[8], ben[9], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    ind = np.arange(n)  # the x locations for the groups
    width = 0.50  # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, benford_means, width)
    p2 = plt.bar(ind, data_means, width, bottom=benford_means)

    plt.ylabel('Percentages')
    plt.title('Benford\'s law comparison')
    plt.xticks(ind, ('1', '2', '3', '4', '5', '6', '7', '8', '9', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9'))
    plt.yticks(np.arange(0, 40, 2.5))
    plt.legend((p1[0], p2[0]), ('Benfors\'s', 'Our Data'))

    plt.show()


csv_list = read_csv('stocks.csv')
first_digit_list = get_first_digit(csv_list)
first_occurrence_dict = assign_first_digits(first_digit_list)
digits_percentage_dict = digits_percentage(first_occurrence_dict, len(first_digit_list))
show_graphs(digits_percentage_dict, benford_law)
