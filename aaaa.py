def test1(lista):
    guest_list = list(
        map(
            lambda g: {
                "name": g.full_name,
                "age": g.age,
                "type": "child" if g.is_child else "adult",
            },
            lista,
        )
    )
    return guest_list


def test2(lista):
    return [
        {
            "name": guest.full_name,
            "age": guest.age,
            "type": "child" if guest.is_child else "adult"
        }
        for guest in lista
    ]


if __name__ == "__main__":
    lista = [
        {
            "full_name": "John Doe",
            "age": 18,
            "is_child": False
        },
        {
            "full_name": "Jane Doe",
            "age": 17,
            "is_child": True
        },
        {
            "full_name": "John Smith",
            "age": 12,
            "is_child": True
        },
        {
            "full_name": "Jane Smith",
            "age": 10,
            "is_child": True
        },
        {
            "full_name": "John Wayne",
            "age": 8,
            "is_child": True
        },
        {
            "full_name": "Jane Wayne",
            "age": 6,
            "is_child": True
        },
    ]

    list_as_objects = [
        type("Guest", (object,), guest) for guest in lista
    ]
    print(test1(list_as_objects))
    print(test2(list_as_objects))
