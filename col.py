#fro generating color
def col():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))