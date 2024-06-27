# Baseball-Team-Manager-V4


Team Management Program: Version 4
Use a database to store the data for the Baseball Team Manager program. The user interface and objects class will change very little. This is an exercise in changing the data layer tier with minimal changes to the interface and business logic tiers.
Player table sql script 
The following is the sql script that can be used to create the sqlite database table. This script is provided only to illustrate how the database is created and is not used in the program. The “player_db.sqlite” file required for the project is included on the assignment page. Keep a backup copy of the sqlite file in case the data  becomes corrupted. If the file is 0KB replace it with a copy of the backup. Note that the Player table has a playerID and batOrder field. The Player class will need to be updated to have a playerID attribute and batOrder attribute.
-- Drop the table if it already exists
DROP TABLE IF EXISTS Player;

-- Create the table
CREATE TABLE Player(
    playerID    INTEGER PRIMARY KEY     NOT NULL,
    batOrder    INTEGER                 NOT NULL,
    firstName   TEXT                    NOT NULL,
    lastName    TEXT                    NOT NULL,
    position    TEXT                    NOT NULL,
    atBats      INTEGER                 NULL,
    hits        INTEGER                 NULL
);
-- Populate the table
INSERT INTO Player VALUES
(1,1,'Dominick','Gilbert','1B',537,170),
(2,2,'Craig','Mitchel','CF',396,125),
(3,3,'Jack','Quinn','RF',545,99),
(4,4,'Simon','Harris','C',450,135),
(5,5,'Darryl','Moss','3B',501,120),
(6,6,'Grady','Guzman','SS',443,131),
(7,7,'Wallace','Cruz','LF',443,131),
(8,8,'Cedric','Cooper','2B',165,54),
(9,9,'Alberto','Gomez','P',72,19);

DB Specifications
•	Modify the db module so that it provides all functions necessary to work with the player data. This should include functions for reading all players, adding a player, deleting a player, updating the batting order for all players, and updating the data for a player.
•	To update multiple columns for a single row, you can use an SQL statement like this:
UPDATE Player
SET position = ?,
    atBats = ?,
    hits = ?
WHERE playerID = ?
Sample Console Output
================================================================
                   Baseball Team Manager

CURRENT DATE:    2020-09-12
GAME DATE:       2020-09-19
DAYS UNTIL GAME: 7

MENU OPTIONS
1 – Display lineup
2 – Add player
3 – Remove player
4 – Move player
5 – Edit player position
6 – Edit player stats
7 - Exit program

POSITIONS
C, 1B, 2B, 3B, SS, LF, CF, RF, P
============================================================ 
Menu option:  1
   Player                            POS    AB     H     AVG
------------------------------------------------------------
1  Dominick Gilbert                   1B   545   170   0.317
2  Craig Mitchell                     CF   396   125   0.316
3  Jack Quinn                         RF   345    99   0.287
4  Simon Harris                        C   450   135   0.300
5  Darryl Moss                        3B   501   120   0.240
6  Grady Guzman                       SS   463   114   0.246
7  Wallace Cruz                       LF   443   131   0.296
8  Cedric Cooper                      2B   165    54   0.327
9  Alberto Gomez                       P    72    19   0.264

Menu option:

General Specifications
•	Use a Player class that provides attributes that store the playerID, batOrder, first name, last name, position, at bats, and hits for a player. The class constructor should use these seven attributes as parameters. This class should also provide a method that returns the full name of a player and a method that returns the batting average for a player. 
•	The playerID is not used when adding a player to the lineup. A PlayerID, the primary key for the Player table, is automatically created by the database.
•	Use a Lineup class to store the lineup for the team as a private list of player objects. This class should include methods with appropriate parameters that allow you to add, remove, move, and edit a player. In addition, it should include an iterator method so you can easily loop through each player in the lineup. A Lineup object replaces the list that holds all players.
•	Use the same console Input/output code that was used in project 3. The module file for this system will be named UI. See the template for the overall design.
•	Use a module file named Objects to store the code for the Player and Lineup classes.
•	Use a file named db.py to store the functions that work with the file that stores the data. A db_comments.py file is included as a template for the DB file that must be turned in. It has a main module that can be used to test the ‘get_players’ method.
Submission details
Projects can require the use of material from any of the previous chapters covered in the textbook.
Create a Team Management Python program that satisfies the specifications above. 
Put General Comments at the beginning of the project that includes (1) your name, (2) the project name, (3) the date, and (4) a description of the project. 
Turn in a ZIP file of the final version of the program. Include a Word document which contains output of the testing done on the program. The Word document must be inside the ZIP file.
In the Comments section on the Assignment webpage, report (A) an estimate of the time it took to complete the project. Report a single value in minutes, and (B) a single rating of the project, on an ordinal scale, as either (1) Easy, (2) Moderate, (3) Hard, OR (4) Challenging. 
