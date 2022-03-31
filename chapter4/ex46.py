def computepay(h, r):
    if h <= 40:
        pay = h * r
    else:
        workingHourPay = 40 * r
        overTimePay = (h - 40) * 1.5 * r
        pay = workingHourPay + overTimePay
    return pay

hours = input("Enter Hours:")
rate = input("Enter Rate:")

hours = float(hours)
rate = float(rate)

p = computepay(hours, rate)
print("Pay", p)