from app.database.models.sport import SportsModel

l = [SportsModel(1, "sambo1"), SportsModel(1, "sambo"), SportsModel(2, "box")]
d={}
k = []
v = ''
for i in l:
    if i.id not in d:
        d[i.id] = []
    t = []
    t.append(i.sport)
    t.append(i.sport)
    d[i.id] = t
    t = []
print(d)