import sqlite3
conn = sqlite3.connect('MovieRecommendationSystem.db')
cursor = conn.cursor()

movies = [
    
        ("Warfare", 95, "Action", "Alex Garland, Ray Mendoza", "D'Pharaoh Woon-A-Tai, Will Poulter, Cosmo Jarvis", "R", 78, "A platoon of Navy SEALs embark on a dangerous mission in Ramadi, Iraq, with the chaos and brotherhood of war retold through their memories of the event."),
        ("Sinners", 137, "Horror", "Ryan Coogler", "Michael B. Jordan, Jack O'Connell, Hailee Steinfeld", "R", 84, "Trying to leave their troubled lives behind, twin brothers return to their hometown to start again, only to discover that an even greater evil is waiting to welcome them back."),
        ("Bring Her Back", 104, "Horror", "Danny Philippou, Michael Philippou", "Billy Barratt, Sally Hawkins, Mischa Heywood", "R", 75, "A brother and sister uncover a terrifying ritual at the secluded home of their new foster mother."),
        ("Mission Impossible: The Final Reckoning", 169, "Action", "Christopher McQuarrie", "Tom Cruise, Hayley Atwell, Ving Rhames", "PG-13", 67, "Hunt and the IMF pursue a dangerous AI called the Entity that's infiltrated global intelligence. With governments and a figure from his past in pursuit, Hunt races to stop it from forever changing the world."),
        ("Thunderbolts*", 127, "Action", "Jake Schreier", "Florence Pugh, Sebastian Stan, Julia Louis-Dreyfus", "PG-13", 68, "After finding themselves ensnared in a death trap, an unconventional team of antiheroes must go on a dangerous mission that will force them to confront the darkest corners of their pasts."),
        ("Black Bag", 93, "Thriller", "Steven Soderbergh", "Michael FassbenderGustaf SkarsgårdCate Blanchett", "R", 85, "When intelligence agent Kathryn Woodhouse is suspected of betraying the nation, her husband - also a legendary agent - faces the ultimate test of whether to be loyal to his marriage, or his country."),
        ()
    
]



#title, duration, genre, director, actors, classification, metascore, concise summary  time in mins
