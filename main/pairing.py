import random

"""
This module is designed to load and generate Swiss style pairings from a given input
It is assumed that this input will be a json input from the main program and should
be stored in something outside of memeory like a database to avoid impacting perfomance
"""

"""
The data structure is assumed to be as such at the beginning of round one:
{
    "players": #list of players in the event
    {
        1: #event player ID
        {
            "player_name":"John Doe", #Players name
            "player_id":1001 #Players global ID number (see database code)
            "player_faction":"Angry Dudes", #Faction that the player is playing. This is recorded to attempt to avoid mirror matches
            "wld": #Win loss draw count
                {
                    "wins":0,
                    "loses":0,
                    "draws":0
                },
            "victory_points":0, #total number of victory points
            "dropped":False, #If the current player is dropped or not
            "previous_opponents":[] #This is a list of previous opponents, its mainly to avoid uneeded rematches. Shouldn't be a problem in Swiss pairing
        },
        2:
        {
            "player_name":"Jane Doe", #Players name
            "player_id":1324 #Players global ID number (see database code)
            "player_faction":"Zombie Bros", #Faction that the player is playing. This is recorded to attempt to avoid mirror matches
            "wld": #Win loss draw count
                {
                    "wins":0,
                    "loses":0,
                    "draws":0
                },
            "victory_points":0, #total number of victory points
            "dropped":False, #If the current player is dropped or not
            "previous_opponents":[] #This is a list of previous opponents, its mainly to avoid uneeded rematches. Shouldn't be a problem in Swiss pairing
        },
        3:
        {...},
        ...
    },
    "tables": #a list of tables with their scenario
    {
        1:"Punch him in the face",
        2:"Dont get punched in the face",
        ...
    }
}