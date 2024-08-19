# importantando biblioteca
import calendar
from datetime import date

# #exibindo a data atual
# print(date.today())

# declaração de variáveis
dia = date.today().day
mes = date.today().month
ano = date.today().year

# tupla dos meses do ano
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# saída de dados
print(f'Data atual: {dia} de {meses[mes - 1]} de {ano}.\n')
print('Mês atual')
print(calendar.month(ano, mes))
