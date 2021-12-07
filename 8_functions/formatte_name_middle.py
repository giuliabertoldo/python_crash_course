# 8.3 RETURN VALUES
## PAG. 139

def formatted_name(first_name, last_name, middle_name = ""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = formatted_name('jimi', 'hendrix')
print(musician)

musician = formatted_name('jimi', 'hooker', 'hendrix')
print(musician)
