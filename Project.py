import random
st = True
while st == True:
    try:
        n = int(input("Number of rolls: "))
        if 1 <= n <= 1000:
            roll = [random.randint(1,6) for i in range(n)]


            print("Rolls: ", end="")
            for i in roll:
                print(i,end=" ")

            print()
            print(f"Frequency: 1:{roll.count(1)} | 2:{roll.count(2)} | 3:{roll.count(3)} | 4:{roll.count(4)} | 5:{roll.count(5)} | 6:{roll.count(6)}")

            print(f"Total: {sum(roll)} | Average: {(sum(roll))/n:.2f}")



            highest = max(roll.count(i) for i in range(1,7))
            winners = [i for i in range(1,7) if roll.count(i) == highest]

            if len(winners) == 1 and highest == 1:
                print(f"Most frequent: {winners[0]} ({highest} time)")
            elif len(winners) == 1:
                print(f"Most frequent: {winners[0]} ({highest} times)")
            elif highest == 1:
                names = " and ".join(str(i) for i in winners)
                print(f"Most frequent: {names} ({highest} time each)")
            else:
                names = " and ".join(str(i) for i in winners)
                print(f"Most frequent: {names} ({highest} times each)")




            s = input("Play again? ")
            if s == "n":
                st = False
                break
        else:
            print("Invalid input. Enter a whole number from 1 to 1000")
    except ValueError:
        print("Invalid input. Enter a whole number from 1 to 1000")

print("Thanks for playing!")