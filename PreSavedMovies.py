import sqlite3
conn = sqlite3.connect('MovieRecommendationSystem.db')
cursor = conn.cursor()

movies = [
    
        ("Warfare", 95, "Action", "Alex Garland, Ray Mendoza", "D'Pharaoh Woon-A-Tai, Will Poulter, Cosmo Jarvis", "R", 78, "A platoon of Navy SEALs embark on a dangerous mission in Ramadi, Iraq, with the chaos and brotherhood of war retold through their memories of the event."),
        ("Sinners", 137, "Horror", "Ryan Coogler", "Michael B. Jordan, Jack O'Connell, Hailee Steinfeld", "R", 84, "Trying to leave their troubled lives behind, twin brothers return to their hometown to start again, only to discover that an even greater evil is waiting to welcome them back."),
        ("Bring Her Back", 104, "Horror", "Danny Philippou, Michael Philippou", "Billy Barratt, Sally Hawkins, Mischa Heywood", "R", 75, "A brother and sister uncover a terrifying ritual at the secluded home of their new foster mother."),
        ("Mission Impossible: The Final Reckoning", 169, "Action", "Christopher McQuarrie", "Tom Cruise, Hayley Atwell, Ving Rhames", "PG-13", 67, "Hunt and the IMF pursue a dangerous AI called the Entity that's infiltrated global intelligence. With governments and a figure from his past in pursuit, Hunt races to stop it from forever changing the world."),
        ("Thunderbolts*", 127, "Action", "Jake Schreier", "Florence Pugh, Sebastian Stan, Julia Louis-Dreyfus", "PG-13", 68, "After finding themselves ensnared in a death trap, an unconventional team of antiheroes must go on a dangerous mission that will force them to confront the darkest corners of their pasts."),
        ("Black Bag", 93, "Thriller", "Steven Soderbergh", "Michael FassbenderGustaf SkarsgardCate Blanchett", "R", 85, "When intelligence agent Kathryn Woodhouse is suspected of betraying the nation, her husband - also a legendary agent - faces the ultimate test of whether to be loyal to his marriage, or his country."),
        ("One of Them Days", 97, "Comedy", "Lawrence Lamont","Keke Palmer, SZA, Vanessa Bell Calloway", "R", 73, "When best friends and roommates Dreux and Alyssa discover Alyssa's boyfriend has blown their rent money, the duo finds themselves going to extremes in a race against the clock to avoid eviction and keep their friendship intact." ),
        ("The Monkey", 98, "Horror", "Osgood Perkins", "Theo James, Tatiana Maslany, Christian Convery", "R", 62, "When twin brothers Bill and Hal find their father's old monkey toy in the attic, a series of gruesome deaths start. The siblings decide to throw the toy away and move on with their lives, growing apart over the years."),
        ("Companion", 97, "Sci-Fi", "Drew Hancock", "Sophie Thatcher, Jack Quaid, Lukas Gage", "R", 70, "A weekend getaway with friends at a remote cabin turns into chaos after it's revealed that one of the guests is not what they seem."),
        ("The Ritual", 98, "Horror", "David Midell", "Al Pacino, Dan Stevens, Ashley Greene", "N/A", "Two priests, one in crisis with his faith and the other confronting a turbulent past, must overcome their differences to perform a risky exorcism."),
        ("Cleaner", 97, "Thriller", "Martin Campbell", "Poppy Townsend White, Dudley Watts, Calvin Warrington-Heasman", "R", 51, "Criminal activists hijack a gala, taking 300 hostages. One extremist plans mass murder as a message to the world. An Ex-soldier turned window cleaner now works to rescue the hostages."),
        ("Death of a Unicorn", 107, "Horror", "Alex Scharfman", "Paul Rudd, Jenna Ortega, Will Poulter","R", 51, "A father and daughter accidentally hit and kill a unicorn while en route to a weekend retreat, where his billionaire boss seeks to exploit the creature's miraculous curative properties."),
        ("Inheritance", 101, "Thriller", "Neil Burger", "Phoebe Dynevor, Rhys Ifans, Jose Alvarez", "R", 55, "When a young woman learns her father was once a spy, she suddenly finds herself at the center of an international conspiracy."),
        ("Chainsaw Man - The Movie: Reze Arc", 100, "Action", "Tatsuya Yoshihara", "Kikunosuke ToyaShiori IzawaTomori Kusunoki", "R", 71, "A direct sequel to the first season of the series "Chainsaw Man", featuring Denji, a young man who co-exists with a chainsaw demon. Denji encounters a new romantic interest, but will his involvement place them both in danger?"),
        ("The Fantastic Four: First Steps", 115, "Sci-Fi", "Matt Shakman", "Pedro Pascal, Vanessa Kirby, Ebon Moss-Bachrach", "PG - 13", 65, "Forced to balance their roles as heroes with the strength of their family bond, the Fantastic Four must defend Earth from a ravenous space god called Galactus and his enigmatic herald, the Silver Surfer."),
        ("Superman", 129, "Action", "James Gunn", "David Corenswet, Rachel Brosnahan, Nicholas Hoult", "PG - 13", 68, "Superman must reconcile his alien Kryptonian heritage with his human upbringing as reporter Clark Kent. As the embodiment of truth, justice and the American way he soon finds himself in a world that views these as old-fashioned."),
        ("Happy Gilmore 2", 114, "Comedy", "Kyle Newacheck", "Adam Sandler, Julie Bowen, Christopher McDonald", "PG - 13", 52, "To provide for his family, a retired Happy Gilmore must pick up the golf clubs once more and reconnect with the sport he once dominated."),
        
    
]



#title, duration, genre, director, actors, classification, metascore, concise summary  
#duration is in minutes