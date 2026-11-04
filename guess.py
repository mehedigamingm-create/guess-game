import random
number = random.randint(1, 100)
guess = 0
while guess != number:
    guess = int(input("Shonkha ta ki (1-100)? "))
    if guess < number:
        print("Aro boro shonkha diben")
    elif guess > number:
        print("Aro choto shonkha diben")
print("Thik dhoreche! Shonkha ta chilo", number)

