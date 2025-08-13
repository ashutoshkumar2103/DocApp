def getdata():
    with open('name.txt') as file:

        names = file.read()

        names = names.split()

        return names