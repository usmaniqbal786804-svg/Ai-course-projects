import colorama
from colorama import Fore, Style
from textblob import TextBlob
import time


colorama.init()


history_list = []
pos_count = 0
neg_count = 0
neu_count = 0


def show_processing_animation():
    """Displays a basic spy loading loop."""
    print(Fore.CYAN + "🕵️ Spy analyzing", end="")
    
    for i in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print(Style.RESET_ALL + "\n")


def analyze_sentiment(text):
    """Calculates sentiment using TextBlob and updates global variables."""
    global pos_count, neg_count, neu_count
    
   
    polarity = TextBlob(text).sentiment.polarity
    
    
    if polarity > 0.25:
        sentiment_type = "Positive"
        pos_count = pos_count + 1
    elif polarity < -0.25:
        sentiment_type = "Negative"
        neg_count = neg_count + 1
    else:
        sentiment_type = "Neutral"
        neu_count = neu_count + 1
        
    return polarity, sentiment_type


def execute_command(command):
    """Processes simple textual control commands."""
    global history_list, pos_count, neg_count, neu_count
    
    if command == "help":
        print(Fore.CYAN + "Available Commands:")
        print("help    -> Lists available commands.")
        print("summary -> Displays the sentiment analysis summary.")
        print("history -> Displays all previous messages.")
        print("reset   -> Resets all stored data.")
        print("exit    -> End the chat and save data." + Style.RESET_ALL + "\n")
        
    elif command == "summary":
        print(Fore.CYAN + "--- Sentiment Summary ---")
        print(Fore.GREEN + "Positive: " + str(pos_count))
        print(Fore.RED + "Negative: " + str(neg_count))
        print(Fore.YELLOW + "Neutral: " + str(neu_count) + Style.RESET_ALL + "\n")
        
    elif command == "history":
        if len(history_list) == 0:
            print(Fore.YELLOW + "No conversation history yet." + Style.RESET_ALL + "\n")
        else:
            print(Fore.CYAN + "--- History Logs ---" + Style.RESET_ALL)
            for item in history_list:
                print("Text: " + item[0] + " | Sentiment: " + item[1] + " | Polarity: " + str(item[2]))
            print("")
            
    elif command == "reset":
        history_list.clear()
        pos_count = 0
        neg_count = 0
        neu_count = 0
        print(Fore.CYAN + "All history and counters reset!" + Style.RESET_ALL + "\n")


def get_valid_name():
    """Forces user to enter a name using only alphabetic letters."""
    while True:
        name_input = input(Fore.MAGENTA + "Please enter your name: " + Style.RESET_ALL).strip()
        
       
        if name_input.isalpha() == True:
            return name_input
            
        print(Fore.RED + "Error: Use alphabetic characters only!" + Style.RESET_ALL)



print(Fore.CYAN + " Welcome to Sentiment Spy! " + Style.RESET_ALL)
user_name = get_valid_name()

print("\nHello, Agent " + user_name + "!")
print("Type any text sentence for sentiment analysis, or use a system command.")
print("Commands: help, summary, history, reset, exit\n")

running = True
while running == True:
    user_input = input(Fore.GREEN + ">> " + Style.RESET_ALL).strip()
    
   
    if user_input == "":
        print(Fore.RED + "Please type something." + Style.RESET_ALL)
        continue

    lower_input = user_input.lower()
    
 
    if lower_input == "exit":
        print("\nExiting Sentiment Spy. Farewell, Agent " + user_name + "!")
        running = False
        continue
        

    if lower_input == "help" or lower_input == "summary" or lower_input == "history" or lower_input == "reset":
        execute_command(lower_input)
        continue
        
 
    show_processing_animation()
    score, result_type = analyze_sentiment(user_input)
    
   
    history_list.append([user_input, result_type, score])
    

    if result_type == "Positive":
        print(Fore.GREEN + " Positive sentiment detected! Polarity score: " + str(score) + Style.RESET_ALL + "\n")
    elif result_type == "Negative":
        print(Fore.RED + " Negative sentiment detected! Polarity score: " + str(score) + Style.RESET_ALL + "\n")
    else:
        print(Fore.YELLOW + " Neutral sentiment detected! Polarity score: " + str(score) + Style.RESET_ALL + "\n")



print("\n====================================")
print("        FINAL SUMMARY REPORT        ")
print("====================================")
print("Positive Messages: " + str(pos_count))
print("Negative Messages: " + str(neg_count))
print("Neutral Messages: " + str(neu_count))
print("====================================")

filename = user_name + "_sentiment_analysis.txt"
text_file = open(filename, "w", encoding="utf-8")

text_file.write("====================================\n")
text_file.write("SENTIMENT ANALYSIS REPORT FOR AGENT: " + user_name + "\n")
text_file.write("====================================\n")
text_file.write("Total Positive Messages: " + str(pos_count) + "\n")
text_file.write("Total Negative Messages: " + str(neg_count) + "\n")
text_file.write("Total Neutral Messages: " + str(neu_count) + "\n")
text_file.write("====================================\n")

text_file.close()

print(Fore.GREEN + "\nReport saved locally inside: " + filename + Style.RESET_ALL)