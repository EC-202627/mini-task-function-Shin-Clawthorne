
def calculate_fine(bt , do , dr = 5.0 , mf = 150.0):
    fine = do * dr
    if fine > mf:
        fine = mf
    return fine

bt = input()
days = int(input())
rate = float(input())
fine = calculate_fine(bt , days , rate)

print(f"Book: {bt}")
print(f"Days overdue: {days}")
print(f"Fine: Rs. {fine}")