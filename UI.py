# Sebastian Sloan
# Project 4 
# December 10, 2023 
# update project with new material learned over the past 14 weeks


import DB
from datetime import date
import datetime
from Objects import *

def display_menu():
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    print()
    print("POSITIONS: ")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")
    print('+' * 50) 
    print()

def display_lineup(player_list):
        
    header = ['', 'Player', 'POS', 'AB', 'H', 'AVG']
        
    print("{: <5} {: <38} {: <7} {: <6} {: <5} {: <6}".format(*header))
    print("-" * 80)

    for player in player_list:


        data = [player_list.getLineupNumber(),
                player.getFullName(),
                player.getPosition(),
                player.getAtBats(),
                player.getHits(),
                round(player.getBattingAverage(),3)]

        print("{:<4} {:<40} {: <5} {:<5} {:<5} {:<5}".format(*data))
    print()

def add_player():

    positions = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')

    bat_order = input("please enter players bat order: ")
    first_name = input("Please enter players First Name: ")
    last_name = input("Please enter players Last Name: ")
    position = input("Please enter players position: ")

    while position not in positions:
        print(f"'{position}' is not a valid position, please check the list again and re-enter a valid position.\n")
        print(positions)
        position = input("Position: ")
        print()

    at_bats = input("Please enter players At Bat: ")

    if at_bats.isdigit() == False:
        print("You must enter a positive number, please try again")
        at_bats = input("At Bats: ")
        print()
    elif float(at_bats) < 0:
        print("You must enter a positive number, please try again")
        at_bats = input("At Bats: ")
        print()

    hits = input("Please enter players Hits: ")
    print()

    if hits.isdigit() == False:
        print("You must enter a positive number, please try again")
        hits = input("Hits: ")
        print()

    elif float(hits) > float(at_bats):
        print("This number is not valid, your 'At Bats' score must be higher.")
        hits = input("Hits: ")
        print()

    elif float(hits) < 0:
        print("You must enter a positive number, please try again")
        hits = input("Hits: ")
        print()


    player = Player(bat_order = bat_order, first_name = first_name, last_name = last_name, position = position, 
                    at_bats = at_bats, hits = hits)
    
    DB.add_player(player)
    print()

def remove_player():

    player_to_remove = input("Enter a Player ID: ")

    DB.delete_player(player_to_remove)


def move_player(lineup):
    
    player_to_be_moved = input("please input the Player ID of the player you wish to move: ")

    for player in lineup:
        if str(player.getPlayerID()) == str(player_to_be_moved):
            new_bat_order = input("Please select the new bat order for your player: ")
            player.setBatOrder(str(new_bat_order))

    DB.update_bat_order(lineup)

def edit_player_position(lineup):
    
    
    positions = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')

    player_ID = input("Please enter the players ID number who's position you wish to edit: ")
    print()

    for player in lineup:
        if str(player_ID) == str(player.getPlayerID()):
            new_position = input("Please enter the new position for this player: ")
            if new_position in positions:
                player.setPosition(new_position)
    
    DB.update_player(player)


def edit_player_stats(lineup):

    player_ID = input("Please enter the player ID who's stats you would like to update: ")

    for player in lineup:
        if str(player_ID) == player.getPlayerID():
            at_bats = input("Please enter a 'At Bats' number: ")
            player.setAtBat(at_bats)
            print()
            hits = input("Please enter a 'Hits' number: ")
            player.setHits(hits)

    DB.update_player(player)


def main():
    print('-' * 50) 
    header = "Baseball Team Manager"
    print(header.center(50))
    print()

    date_format = '%Y-%m-%d'

    print(f"CURRENT DATE:    {date.today()}")

    game_date = input("GAME DATE:    ")

    try:

        game_day = datetime.datetime.strptime(game_date, date_format)
        today = datetime.datetime.strptime(str(date.today()), date_format)

        time_to_next_game = game_day - today
        print(f"DAYS UNTIL GAME: {time_to_next_game.days}")

    except ValueError:

        print("Incorrect data format, should be YYYY-MM-DD")
 
    print()
    display_menu()

    DB.connect()

    lineup = DB.get_players()

    while True:
        command = input("Menu option: ")
        if command == "1":
            display_lineup(lineup)
        elif command == "2":
            add_player()
        elif command == "3":
            remove_player()
        elif command == "4":
            move_player(lineup)
        elif command == "5":
            edit_player_position(lineup)
        elif command == "6":
            edit_player_stats(lineup)
        elif command == "7":
            print("Bye!")
            break
        else:
            print("The command you inputted is not a valid command please try again.")
            display_menu()
            print()
            command = input("Menu option: ")


if __name__ == "__main__":
    main()
