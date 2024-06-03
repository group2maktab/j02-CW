speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
speed_value = []
for value in speed.values():
    if value not in speed_value:
        speed_value.append(value)
print(speed_value)
