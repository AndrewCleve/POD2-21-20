def getRealFloor(amfloor):
    amfloor = int(amfloor)
    if(amfloor > 13): amfloor = amfloor-1
    if(amfloor > 0): amfloor = amfloor-1
    return amfloor
    
def main():
    getfinp = input("Get the real floor number from: ")
    try:
        print(getRealFloor(getfinp))
    except ValueError:
        print("That wasn't a number! Try again")
    
if __name__ == "__main__":
    main()