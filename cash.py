from cs50 import get_float


def main():
    dollars= get_inp()
    c=round(dollars*100) #calculating cents
    quaters = int(c/25)  # no. of quaters  (considers quotient of a/25)
    dimes = int((c % 25)/10)  # Remainder of previous division further divided by new denomination
    nickels = int(((c % 25)%10)/5)
    pennies = int((((c % 25)%10)%5)/1)
    coins = quaters + dimes + nickels + pennies
    print(coins)
    

def get_inp():
    while True:
        n = get_float("Change owed: ")
        if n > 0 :
            break
    return n

main()
