bill = input('Hey bitch how much ive got paid this time: ')
percentage_raw = input('How much u would give this poor bastard? 10, 12, or 15 hum?  ')
how_many = input('Yo wheres the gang bitch, how many are left? ')

ten_percent = 1.10
twelf_percent = 1.12
fiveteen_percent = 1.15

payment_each = float(bill) / int(how_many)
if percentage_raw == 10:
    payment = payment_each * twelf_percent
elif percentage_raw == 12:
    payment = payment_each * twelf_percent
elif percentage_raw == 15:
    payment = payment_each * twelf_percent
else:
    pass

print(round(payment, 2))
