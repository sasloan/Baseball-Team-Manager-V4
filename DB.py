import sqlite3
from contextlib import closing
from Objects import *

conn = None


def connect():
    global conn
    if not conn:
        DB_FILE = "player_db.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row


def close():
    if conn:
        conn.close()


def get_players():
    # SQL statement to select all 7 fields for all players
    query = '''
            SELECT *
            FROM Player
            '''
    
    # Use a with statement to execute the query
    with closing(conn.cursor()) as c:
        c.execute(query)
        players = c.fetchall()

    # Create a lineup object
        lineup = Lineup()

    # use a loop to populate the lineup object with player objects
    
        for player in players:
            player_ID = player[0]
            bat_order = player[1]
            first_name = player[2]
            last_name = player[3]
            position = player[4]
            at_bats = player[5]
            hits = player[6]

            player = Player(player_ID, bat_order, first_name, last_name, position, at_bats, hits)

            lineup.addPlayer(player)

        # return the lineup object
        return lineup


        

def get_player(playerID):

    # SQL statement to select all 7 fields for a player
    query = f'''
            SELECT *
            FROM Player
            WHERE PlayerID = {playerID}
            '''
    
    #  Use a with statement to execute the query & return a player object if the player exists
    with closing(conn.cursor()) as c:
        c.execute(query)
        player = c.fetchall()
    
    return player

def add_player(player):
    # SQL statement to insert 6 fields for a player added to the table
    query = '''INSERT INTO Player (batOrder, firstName, lastName, position, atBats, hits)
            VALUES (?,?,?,?,?,?);'''
    
    # Use a with statement to execute the query
    with closing(conn.cursor()) as c:
        c.execute(query, (player.getBatOrder(), player.getFirstName(), player.getLastName(), player.getPosition(), 
                          player.getAtBats(), player.getHits()))
        conn.commit()
        
def delete_player(player_ID):
    # SQL statement to delete a single player
    query = '''DELETE FROM Player WHERE playerID = ?'''

    # Use a with statement to execute the query
    with closing(conn.cursor()) as c:
        c.execute(query, (player_ID))
        test = conn.commit()


def update_bat_order(lineup):
    # Use a loop to call a SQL statement that updates
    # the batOrder for each player based on their playerID
    for player in lineup:
        query = f'''UPDATE Player 
                   SET batOrder = {player.getPlayerID()}'''

    # Use a with statement to execute the query
        with closing(conn.cursor()) as c:
            c.execute(query)
            conn.commit()

def update_player(player):
    # SQL statement to update 6 fields of a player based on the playerID
    query = f'''UPDATE Player
               SET batOrder = ?, firstName = ?, lastName = ?, position = ?, atBats = ?, hits = ?
               WHERE {player.getPlayerID()}'''

    # Use a with statement to execute the query
    with closing(conn.cursor()) as c:
        c.execute(query, (player.getBatOrder(), player.getFirstName(), player.getLastName(), player.getPosition(), 
                          player.getAtBats(), player.getHits()))
        conn.commit()

# def main():
#     # code to test the get_players function
#     connect()
#     players = get_players()
#     if players != None:
#         for player in players:
#             print(player.getBatOrder(), player.getFirstName(), player.getLastName(),
#                   player.getPosition(), player.getAtBats(), player.getHits(), player.getBattingAverage())
#     else:
#         print("Code is needed for the get_players function.")

# if __name__ == "__main__":
#     main()
