"""
1. Реализовать скрипт, в котором должна быть предусмотрена
функция расчета заработной платы сотрудника. В расчете необходимо
использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--name', type = str)
parser.add_argument('--hour', type = int)
parser.add_argument('--rate', type = int)
parser.add_argument('--bonus', type = int, default=50000)

args = parser.parse_args()
print(f"Hello, {args.name}! Нour salary is {args.hour * args.rate + args.bonus}.")
