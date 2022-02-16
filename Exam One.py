from random import randint

username = str(input("Hello! What is your name? "))
print("Well, {}, I am thinking of a number between 1 and 20.".format(username))
print("You have 5 guesses.")

n = randint(1, 20)
guess = int(input("Take a guess: "))
count = 0
while n != "guess":
  count += 1
  if (count < 5):
    if guess < n:
        print ("Your guess is too low.")
        guess = int(input("Take a guess: "))
    elif guess > n:
        print ("Your guess is too high.")
        guess = int(input("Take a guess: "))
    else:
        print ("Good job, {}! You guessed my number in {} guesses!".format(username,count))
        break
  else:
    print("Nope. The number I was thinking of was",n)
    break