import colorama
from colorama import Fore, Style
from textblob import TextBlob
import re
import time

# Initialize Colorama for console colors
colorama.init()

# Global variables for data tracking
history_list = []
pos_count = 0
neg_count = 0
neu_count = 0


# =====================================================================
# 1. DEFINE MODULAR FUNCTIONS
# =====================================================================

def show_processing_animation():
    """Displays a simple spy loading loop effect."""
    print(Fore.CYAN + " Spy checking records", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print(Style.RESET_ALL + "\n")


def analyze_sentiment(text):
    """Calculates text sentiment polarity via TextBlob.
    
    [NLP Integration Note]: A basic sentiment tracker fails if a user uses 
    sarcasm or complex sentence patterns (e.g., 'Not bad at all!'). 
    True NLP sentiment models can contextualize negation and emotion.
    """
    global pos_count, neg_count, neu_count
    polarity = TextBlob(text).sentiment.polarity
    
    if polarity > 0.25:
        sentiment_type = "Positive"
        pos_count += 1
    elif polarity < -0.25:
        sentiment_type = "Negative"
        neg_count += 1
    else:
        sentiment_type = "Neutral"
        neu_count += 1
        
    return polarity, sentiment_type


def get_valid_name():
    """Ensures name contains only alphabetic characters."""
    while True:
        name_input = input(Fore.MAGENTA + "Please enter your name: " + Style.RESET_ALL).strip()
        if name_input.isalpha():
            return name_input
        print(Fore.RED + "Error: Use alphabetic letters only (no numbers/spaces)." + Style.RESET_ALL)


def check_expanded_topics(user_text):
    """Uses Regular Expressions and keyword lists to look for matching topics.
    
    [NLP Integration Note]: Keyword matching breaks if words are misspelled 
    ('wether') or phrased oddly. Intent Classification via NLP would parse 
    the actual meaning of the sentence regardless of the exact vocabulary.
    """
    text = user_text.lower()
    
    # Topic 1: Weather Request via Regular Expressions
    if re.search(r'\bweather\b|\bforecast\b|\brain\b|\bsun\b', text):
        print(Fore.BLUE + " [Weather Spy]: Current simulation shows clear skies with a 20% chance of rain.")
        print("Tip: Keep your umbrella close just in case!" + Style.RESET_ALL + "\n")
        return True
        
    # Topic 2: News Updates via Keyword Matching Lists
    news_keywords = ["news", "headline", "update", "happening", "story"]
    if any(keyword in text for keyword in news_keywords):
        print(Fore.MAGENTA + " [News Spy]: Top Simulation Headline: 'Global Coffee Shortage Causes Emergency Tech Upgrades.'")
        print("Stay tuned for more updates!" + Style.RESET_ALL + "\n")
        return True
        
    # Topic 3: Local Time via Regular Expressions
    if re.search(r'\btime\b|\bclock\b|\bhour\b|\bzone\b', text):
        print(Fore.YELLOW + " [Time Spy]: Simulating universal timeline clocks.")
        print("London: 08:00 AM | New York: 03:00 AM | Tokyo: 04:00 PM" + Style.RESET_ALL + "\n")
        return True

    return False  # No expanded topics matched


def execute_command(command):
    """Processes core utility control choices."""
    global history_list, pos_count, neg_count, neu_count
    
    if command == "help":
        print(Fore.CYAN + "Available System Commands:")
        print("• help    -> Lists system tools.")
        print("• summary -> Displays collected sentiment metric data counts.")
        print("• history -> Lists analyzed lines.")
        print("• reset   -> Wipes history and resets counters." + Style.RESET_ALL + "\n")
        
    elif command == "summary":
        print(Fore.CYAN + "--- Sentiment Metric Counts ---")
        print(Fore.GREEN + f"Positive: {pos_count}")
        print(Fore.RED + f"Negative: {neg_count}")
        print(Fore.YELLOW + f"Neutral: {neu_count}" + Style.RESET_ALL + "\n")
        
    elif command == "history":
        if not history_list:
            print(Fore.YELLOW + "No history logs saved yet." + Style.RESET_ALL + "\n")
        else:
            print(Fore.CYAN + "--- History Logs ---" + Style.RESET_ALL)
            for idx, item in enumerate(history_list, 1):
                print(f"{idx}. Text: '{item[0]}' | Sentiment: {item[1]} (Score: {item[2]:.2f})")
            print("")
            
    elif command == "reset":
        history_list.clear()
        pos_count = neg_count = neu_count = 0
        print(Fore.CYAN + "System cleaned! Memory storage reset." + Style.RESET_ALL + "\n")


# =====================================================================
# 2. MAIN CHATBOT LOOP & VISUAL FEEDBACK
# =====================================================================

print(Fore.CYAN + "====================================")
print("  Welcome to Sentiment Spy 2.0  ")
print("====================================" + Style.RESET_ALL)

agent_name = get_valid_name()

print(f"\nGreeting Agent {agent_name}!")
print("Enter any sentence to analyze it. Try checking 'weather', 'news', or 'time'!")
print(f"Control Panel Shortcuts: {Fore.YELLOW}help, summary, history, reset, exit{Style.RESET_ALL}\n")

while True:
    user_input = input(Fore.GREEN + ">> " + Style.RESET_ALL).strip()
    
    if user_input == "":
        print(Fore.RED + "Please supply valid console inputs." + Style.RESET_ALL)
        continue
        
    lower_input = user_input.lower()
    
    # Process app exit
    if lower_input == "exit":
        print(f"\n{Fore.BLUE}Closing connection panel. Farewell, Agent {agent_name}! {Style.RESET_ALL}")
        break
        
    # Process base management commands
    if lower_input in ["help", "summary", "history", "reset"]:
        execute_command(lower_input)
        continue
        
    # Run text through expanded conversation filter first
    if check_expanded_topics(user_input):
        continue
        
    # Process standard text sentiment path if no special topic matches
    show_processing_animation()
    score, result_type = analyze_sentiment(user_input)
    
    # Store data entries safely inside the history matrix array list
    history_list.append([user_input, result_type, score])
    
    # Custom text colors using Colorama for chatbot responses
    if result_type == "Positive":
        print(Fore.GREEN + f" Positive mood recognized! Score: {score:.2f}" + Style.RESET_ALL + "\n")
    elif result_type == "Negative":
        print(Fore.RED + f" Negative mood recognized! Score: {score:.2f}" + Style.RESET_ALL + "\n")
    else:
        print(Fore.YELLOW + f" Neutral mood recognized! Score: {score:.2f}" + Style.RESET_ALL + "\n")


# =====================================================================
# 3. FINAL REPORT GENERATION
# =====================================================================

print("\n====================================")
print("         FINAL COMPILATION          ")
print("====================================")
print(f"Positive: {pos_count} | Negative: {neg_count} | Neutral: {neu_count}")
print("====================================")

filename = f"{agent_name}_sentiment_analysis.txt"
with open(filename, "w", encoding="utf-8") as text_file:
    text_file.write("====================================\n")
    text_file.write(f"OFFICIAL REPORT FOR AGENT: {agent_name}\n")
    text_file.write("====================================\n")
    text_file.write(f"Positive Data Hits: {pos_count}\n")
    text_file.write(f"Negative Data Hits: {neg_count}\n")
    text_file.write(f"Neutral Data Hits: {neu_count}\n")
    text_file.write("====================================\n")

print(Fore.GREEN + f"Logs locked and saved locally to: {filename}" + Style.RESET_ALL)
