import pyttsx3 
import speech_recognition
import random

#
computer_mounth = pyttsx3.init()
computer_ear = speech_recognition.Recognizer()
computer = "Hello, I am computer, I want to play Rock Paper Scissor, Do you want to play with me?"
print("Computer:" + computer)
computer_mounth.say(computer)
computer_mounth.runAndWait()

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]
random_number = random.randint(0,2)
	#rock:0, paper:1, scissors:2
computer_pick = options[random_number]			


while True:
	
	with speech_recognition.Microphone() as mic:
	   print ("If you want to quit the game, please say \"quit\"")
	   audio = computer_ear.listen(mic)
	try:
		user_input = computer_ear.recognize_google(audio)
	except: 
		user_input =""
	print("User: " + user_input)

	if user_input == "":
		computer = "Hello, please speak louder"
	elif "yes" in user_input: 
		computer = "yeah, let's play"
		if user_input == computer_pick: 
			computer = "We both win, Do you want to have another round?"
			user_wins +=1
			computer_wins += 1
		elif user_input =="rock" and computer_pick == "scissor":
			computer ="You won! Do you want to have another round?"
			user_wins +=1
		elif user_input =="paper" and computer_pick == "rock":
			computer ="You won! Do you want to have another round?"
			user_wins +=1
		elif user_input =="scissors" and computer_pick == "paper":
			computer ="You won! Do you want to have another round?"
			user_wins +=1
		else:
			computer ="You lost! Do you want to have another round?"
			computer_wins += 1

	elif "no" in user_input: 
		computer = "unfortunately"
		print("Computer:" + computer)
		computer_mounth.say(computer)
		computer_mounth.runAndWait() 
		break
	elif user_input == "quit":
		computer = "You won" + user_wins + "times." + "I won" + computer_wins + "times." + "Bye!, See you next time!"
		print("Computer:" + computer)
		computer_mounth.say(computer)
		computer_mounth.runAndWait() 
		break

	print("Computer:" + computer)
	computer_mounth.say(computer)
	computer_mounth.runAndWait()
