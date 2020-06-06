import csv

from django.shortcuts import render


def read_csv(csv_file):
    data = list()
    with open(csv_file) as file:
        for row in csv.DictReader(file, delimiter=';'):
            data.append(row)
    return data


def read_head(csv_file):
    with open(csv_file) as file:
        for i, row in enumerate(csv.reader(file, delimiter=';')):
            if i == 0:
                for j, item in enumerate(row):
                    if item == 'Суммарная':
                        row[j] = 'Всего'
                return row


DATA = 'inflation_russia.csv'


def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    context = {'data': read_csv(DATA),
               'head': read_head(DATA),
               'length': len(read_head(DATA)) - 1}

    return render(request, template_name,
                  context)
