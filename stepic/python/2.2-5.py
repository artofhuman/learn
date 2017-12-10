import datetime

year, month, day = map(lambda x: int(x), input().split(' '))
days = int(input())

data = datetime.date(year, month, day)
result = data + datetime.timedelta(days=days)
print(result.year, result.month, result.day)
