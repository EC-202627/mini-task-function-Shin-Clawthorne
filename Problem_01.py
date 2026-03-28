
def calculate_fine(bt , do , dr = 5.0 , mf = 150.0):
    fine = do * dr
    if fine > mf:
        fine = mf
    return fine

data = input().split()
bt = " ".join(data[:-1])
days = int(data[-1])

fine = calculate_fine(bt , days)

print(f"book: {bt} Days overdue: {days} Fine: Rs. {fine}")
