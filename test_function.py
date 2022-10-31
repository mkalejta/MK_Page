
def get_formatted_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()

the_name = get_formatted_name("Mikolaj", "Kalejta")
print(the_name)