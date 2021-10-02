#' Simple local Spotify™
#' DS: Gavin South
#' Instructions:
#'   Run everything, then main(). The program is intuitive and will guide you after that.
# ——————————————————————————————————————————————————————————————————————————————————————————————————————— ####
#  Libraries
import string
import random
import pandas as pd
# from PIL import Image
# import time # Note: syntax to get a timed break time.sleep(1.5), 1.5 seconds.
from playsound import playsound # Note: playsound(, False) if you want to do things while playing song. 

# ——————————————————————————————————————————————————————————————————————————————————————————————————————— ####
# Users : In dev Saving User.  Will use SQL.
class user:
    def __init__(self):
        self.u_id = ''.join(random.choice(string.ascii_uppercase) for i in range(5))
        print("What is your full name: \n") 
        self.name = input("  -> ")
        print("What music genres do you like: \n") 
        self.favorite_genres = input("  -> ")
        print("Out of these songs, type the number of the one you like most: \n")
        print_song_list()
        self.favorite_songs = input("  -> ")
    def settings():
        print("Changing your full name: \n") 
        self.name = input("  -> ")
        print("Changing your favorite genres: \n") 
        self.favorite_genres = input("  -> ")
        print("Out of these songs, type the number of the one you like most: \n")
        print_song_list()
        self.favorite_songs = input("  -> ")

def create_new_user():
    user_profiles = pd.read_csv("user_profiles.csv", index_col = [0])
    new = user()
    user_profiles.loc[len(user_profiles.index)] = [len(user_profiles.index), new.u_id, new.name, new.favorite_genres, new.favorite_songs] 
    #user_profiles.to_csv("user_profiles.csv") # Take out comment when ready to run.
    print("\nThank you", new.name)
    print("Your new login id name is", new.u_id, "don't forget it.")
    print("\nNow please, type in that id to sign in and start.")
    return(new)

def edit_user(): 
    # Work in progress, will use a SQL database to 
    # manage and use this data in the future. 

# ——————————————————————————————————————————————————————————————————————————————————————————————————————— ####
# Prints available songs: Working
def print_song_list():
    music_library = pd.read_csv("music_library.csv")
    for i in range(len(music_library)):
        print(i + 1, music_library.loc[i]["title"] + ", by "  + music_library.loc[i]["artist"])

# ——————————————————————————————————————————————————————————————————————————————————————————————————————— ####
# Play Music Functions : Working
def play_favorite_song(current_user):
    music_library = pd.read_csv("music_library.csv")
    print("Here is your favorite song:", 
    music_library.loc[current_user[4]]["title"] + ", by",
    music_library.loc[current_user[4]]["artist"], "\n")
    playsound("sample_length_music/" + music_library.loc[current_user[4]]["song_file_name"])
    print("Now, what would you like to do?")
    menu(current_user)

def play_song_choice(current_user):
    music_library = pd.read_csv("music_library.csv")
    print("Type the number of the song you want to listen to:\n")
    print_song_list()
    a = input("  -> ")
    print("\nNow playing:", 
    music_library.loc[int(a) - 1]["title"] + ", by",
    music_library.loc[int(a) - 1]["artist"], "\n")
    playsound("sample_length_music/" + music_library.loc[int(a) - 1]["song_file_name"])
    print("Now, what would you like to do?")
    menu(current_user)

def shuffle_library(current_user):
    music_library = pd.read_csv("music_library.csv")
    l = list(range(len(music_library)))
    random.shuffle(l)
    for i in range(len(music_library)):
        print("Now playing:", 
        music_library.loc[l[i]]["title"] + ", by",
        music_library.loc[l[i]]["artist"], "\n")
        playsound("sample_length_music/" + music_library.loc[l[i]]["song_file_name"]) 
    print("Now, what would you like to do?")
    menu(current_user)

# ——————————————————————————————————————————————————————————————————————————————————————————————————————— ####
# Display Menu : Working
def menu(current_user):
    print("""
    1. Play your favorite song
    2. Select song from library
    3. Shuffle play entire library
    4. Change your profile preferences and favorites
    5. Quit
    """)
    a = input("   -> ")
    if int(a) not in [1, 2, 3, 4, 5]:
        print("\nSorry try choosing again, there was something wrong with your entry.\n")
        menu()
    elif int(a) == 1: play_favorite_song(current_user)
    elif int(a) == 2: play_song_choice(current_user)
    elif int(a) == 3: shuffle_library(current_user)
    elif int(a) == 4: 
        # current_user.settings()
        print("Feature available in next update...")
        menu(current_user) 
    elif int(a) == 5: 
        print("\nAlright, till next time.")
        exit()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————— ####
# Main : Working
def main():
    print("""
    Welcome to ________ music player.
    If you are new here and don't have a saved profile enter the word 'new'. 
    If you have set up a profile in the past, please enter your five letter id name.
    """)
    a = input("  -> ")
    if a in ["new", "New", "NEW", "knew", "nw", "neww"]:
        create_new_user()
        main()
    user_profiles = pd.read_csv("user_profiles.csv", index_col = [0])
    current_user = user_profiles.query("user_id == @a")
    if len(current_user) < 1:
        print("\nCan't seem to find your profile, try again.")
        main()
    current_user = current_user.loc[0]
    print("Welcome", current_user[2])
    menu(current_user)