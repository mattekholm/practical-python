# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 1
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000


while principal > 0:
    if months < extra_payment_start_month or months > extra_payment_end_month:        
        principal = principal * (1+rate/12) - payment
    else:
        principal = principal * (1+rate/12) - (payment + extra_payment)

    total_paid = total_paid + payment

    print(f'Months: {months}, Total paid: {total_paid:0.2f}, Principal: {principal:0.2f}')

    months = months +1
