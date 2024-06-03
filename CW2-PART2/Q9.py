sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}
old="city"
new="location"
sample_dict[new]=sample_dict.pop(old)
print(sample_dict)