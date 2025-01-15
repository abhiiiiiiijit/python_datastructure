import calendar

m, d, y = input().split(" ")
y = int(y)
m = int(m[1])if m[0]==0 else int(m)
d = int(d[1])if d[0] == 0 else int(d)
day_name = calendar.day_name[calendar.weekday(y, m, d)]
day_name_caps = day_name.upper()
print(day_name_caps)