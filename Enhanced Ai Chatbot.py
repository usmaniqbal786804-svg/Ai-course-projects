print("Hello! I am your AI Bot.")
name = input("What's your name? : ")
print("Nice to meet you, " + name + "!")

choice = "yes"
while choice == "yes":
    mood = input("How are you feeling today? (good/bad): ")
    if mood == "good":
        print("Glad to hear that!")
    elif mood == "bad":
        print("I am sorry to hear that.")
    else:
        print("I see.")
    hobby = input("What is your favorite hobby? : ")
    print("Wow, " + hobby + " sounds like fun!")
    choice = input("Do you want to continue chatting? (yes/no): ")
print("Goodbye " + name + "!")