import collections

results = {'a':60, 'b':70, 'c': 5}

c = collections.Counter(results)

print c.most_common(1)[0][0]
