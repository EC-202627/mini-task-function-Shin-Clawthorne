

def calculate_fine(bt , do , dr = 5.0 , mf = 150.0):
    fine = do * dr
    if fine > mf:
        return mf , True
    return fine , False

bt = input()
days = int(input())

fine , cap= calculate_fine(bt , days)

print(f"Book: {bt}")
print(f"Days overdue: {days}")
print(f"Fine: Rs. {fine}")

if (cap):
    print(f"You have accumulated the maximum fine of INR: 150.0")