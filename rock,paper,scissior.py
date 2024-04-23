import random
Choise=["rock","paper","sessior"]
computer=random.choice(Choise)
while True:
	user=str(input("Enter your choise :> "))
	if user=="rock" and computer=="paper":
		print("paper win !")
	elif user=="paper" and computer=="sessior":
		print("sessior win !")
	elif user=="rock" and computer=="sessior":
		print("rock win")
	else:
		print("draw")