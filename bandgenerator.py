def main ():
    print("Welcome to the Band Name Generator!")
    bandgenerator()

def bandgenerator():
    cityname = input("What's the name of the city you grew up in? ")
    print(cityname)
    petname = input("What's your pet's name? ")
    print(petname)
    print("Your band name could be ", cityname, petname)

main()
