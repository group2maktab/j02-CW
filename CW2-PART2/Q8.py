def extract(input, keys):
    extract_dic = {}    
    for key, value in input.items():
        if key in keys:
            extract_dic[key] = value
    return extract_dic

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}
keys = ["name", "salary"]
extract_dic = extract(sample_dict, keys)
print(extract_dic)

