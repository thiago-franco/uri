x = int(input())
years = x//365
months = x%365//30
days = (x%365)%30
print(years, "ano(s)")
print(months, "mes(es)")
print(days, "dia(s)")
