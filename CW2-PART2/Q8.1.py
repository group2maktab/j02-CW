sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
keys_to_extract = ["name","salary"]
new_dict = {key: sample_dict[key]
for key in sample_dict.keys() & keys_to_extract}
print(new_dict)