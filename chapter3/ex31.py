hrs = input("Enter Hours:")
ratePerHour = input("Enter Rate:")
h = float(hrs)
r = float(ratePerHour)

if (h <= 40):
    grossPay = h * r
else:
    normalPay = 40 * r
    overTime = (h - 40) * r * 1.5
    grossPay = normalPay + overTime

print(grossPay)