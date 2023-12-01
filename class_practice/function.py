def me(name: str, number: int, age: int = 18):
    return number * age


# positional argument
me("Philip", 1234, 67)
# keyword argument
me(age=56, name="Philip", number=3452)
# combination of both keyword and positional argument
me(67, number=6754, name="odey")
