dicionario = {
    "name": "John",
    "age": 18,
    "is_child": False,
    "email": "johj@gmail.com",
    "phone": "123456789",
    "address": "Street 1",
    "city": "City 1",
    "state": "State 1",
    "country": "Country 1",
}

dicionario_as_object = type("Guest", (object,), dicionario)


def get_person_in_string(name, age, phone):
    return f"Name: {name}, Age: {age}, Phone: {phone}"


if __name__ == "__main__":
    pessoa = {}
    pessoa["name"] = "John"
    pessoa["age"] = 18
    pessoa["phone"] = "123456789"
    print(get_person_in_string(
        "John",
        18,
        "123456789"
    ))
    print(get_person_in_string(**pessoa))
