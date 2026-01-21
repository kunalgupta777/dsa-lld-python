"""
PROGRAMMING EXERCISE 
You are encouraged to ask the interviewer questions as you read and after reading.
At Stripe we keep track of where the money is and move money between bank accounts to make sure their balances are not below some threshold. This is for operational and regulatory reasons, e.g. we should have enough funds to pay out to our users, and we are legally required to separate our users' funds from our own. This interview question is a simplified version of a real-world problem we have here.
Let's say there are at most 500 bank accounts, some of their balances are above 100 and some are below. How do you move money between them so that they all have at least 100?
Just to be clear we are not looking for the optimal solution, but a working one.

Example input:

     AU: 80
     US: 140
     MX: 110
     SG: 120
     FR: 70

Output:

from: US, to: AU, amount: 20
from: US, to: FR, amount: 20
from: MX, to: FR, amount: 10

Potential follow ups/parts (in no specific order):
(Practical) If this code will be used to move millions of dollars in production, how would you change it? Specifically, we just eyeballed that our end goal of each balance >= 100 is met, how would you check that in reality? What should we do if the check fails?
(Algorithmic) Do it in the minimum number of moves. For the input data in the original prompt:

from: US, to: FR, amount: 30
from: SG, to: AU, amount: 20

"""

def get_transfers(balances):
    if sum(balances.values()) < len(balances) * 100:
        return None
    
    transfers = [] ## transfers[i] = (from, to, amount)
    balances = sorted(balances.items(), key = lambda x : x[1], reverse = True)
    l, r = 0, len(balances)-1
    while l < r:
        if balances[r][1] >= 100:
            break
        if 100 - balances[r][1] <= balances[l][1] - 100:
            transfers.append((balances[l][0], balances[r][0], 100 - balances[r][1]))
            r-=1
        else:
            l+=1
    return transfers

if __name__ == "__main__":
    balances = {"AU": 80, "US": 140, "MX": 100, "SG": 120, "FR": 70}
    transfers = get_transfers(balances)
    if not transfers:
        print("It's impossible to ensure each account has a minimum balance of 100 with the current balances.")
    elif len(transfers) == 0:
        print("No transfers required, each account already has a minimum balance of 100")
    else:
        print("There are minimum " + str(len(transfers)) + " transfers required to ensure each account has a minimum of 100 balance")
        for frm, t, amt in transfers:
            print("From: " + frm + ", To: " + t + ", Amount: " + str(amt))