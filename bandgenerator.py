def main ():
    print("Welcome to the Band Name Generator!")
    print("We will help you decide on a name for your band.")
    print("First we'll need you to answer a few questions.")
    bandgenerator()

def bandgenerator():
    cityname = input("What's the name of the city you grew up in? ")
    print(cityname)
    petname = input("What's your pet's name? ")
    print(petname)
    favorite_color = input("What's your favorite color? ")
    print("Your band name could be ", cityname, petname, favorite_color)

main()
