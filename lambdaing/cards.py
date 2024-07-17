from classes import *

standard_cards = [
	TACard('Tim Tu, Tuner of Two Tubas', 1500, 1600),
	TACard('λaryn, λord of λambdas', 1500, 1500),
	TACard('Addison, from operator import add', 2000, 1200),
	TutorCard('Maanav, Recursive Royal', 2100, 1100),
	TACard('Ben, Paladin of Penguins and Turtles', 1600, 1600),
	TutorCard('Kevin, writer of inefficient code, the destroyer of worlds', 2000, 1300),
	TutorCard('Kendrick, Local Gardener', 1400, 2000),
	TACard('Grace, Ramen Fairy', 1000, 2300),
	AICard('Eric, the Hollow Knight', 2400, 1000),
	AICard('Sanjay, the Juicer of Lemons', 1001, 2299),
	AICard('Hans, the king of debugger', 1800, 1500),
	AICard('Rebecca, the Patron of Fangirls', 1200, 1700),
	AICard('Reuben, the Bringer of Chaos and Nuggets', 1100, 2100),
	AICard('Albert, Connoisseur of Kpop', 2299, 1001),
	AICard('Frank, the Tank', 1000, 2300),
	AICard('Anniyat, the Tangerine Annihilator', 1600, 1800),
	AICard('Tyler, Shepherd of Lambdas', 1200, 1600),
	AICard('Heather, Oatmeal Oracle', 1000, 2200),
	AICard('Ian, the Nemesis of the Mortals', 1700, 1300),
	AICard('Ashley, Banisher of Sleep', 1800, 1300),
	AICard('Ishaan, Shinobi of the Leaf', 1600, 1600),
	AICard('Praj, Subway Trainer', 2000, 1000),
	AICard('David, the Frost Monarch', 1500, 1000),
	AICard('Rae, Friend of Cats', 1900, 1200),
	AICard('Nikki, Creator of Ships', 1700, 1700),
	AICard('Jonathan, Dryad of Data', 1900, 1400),
	AICard('Ethan, Cookie Monster Supreme', 1000, 2300),
	AICard('Amol, Warrior Unlimited', 2300, 1000),
	TACard('Connie, Consumer of Carbs', 2100, 1000),
	AICard('Sage, the Doom Bot 3000', 1000, 2300),
	AICard('Julia, the Summoner of Chipotle', 1700, 1600),
	AICard('Sameer, Disciple of Hilfinger', 1200, 1600),
	AICard('Sepehr the Pear', 1100, 2000),
	AICard('Karim, Sayer of Many, Doer of None', 1100, 2000),
	TACard('John, Generator of Generators', 1500, 1800),
	AICard('Yoisaki Kanade, The Only Waifu', 1500, 1500),
	AICard('Sid, User of Murphys Law', 2300, 1000),
	AICard('Phillip, the Pyro Primate', 2100, 1300),
	AICard('Michael, the Master of Mozzarella', 1500, 1700),
	AICard('Ashley, Coffee Connoisseur', 1500, 1600),
	TACard('Jamie the Imaginary', 1800, 1500),
	AICard('Aarin, the Analyst ', 1800, 1500),
	AICard('Ritik, Earth Crusher', 2100, 1200),
	AICard('Christopher, the Fatigued Foe', 2000, 1300),
	TACard('Daphne, Pigeon Carrier', 1000, 1500),
	TACard('Jordan, Pigeon Carrier', 1500, 1000),
	TACard('Patrick', 1700, 1400),
	TACard('Shaun the Credit Card Connoisseur', 2300, 1000),
	TACard('Charlotte, Shawarma Sharpshooter', 1200, 2100),
	TutorCard('Mingxiao, QwQ', 1300, 2100),
	AICard('Arjun, Magistrate of Entropy', 2100, 1200),
	AICard('Ted, Seeker of the Truth', 2000, 1100),
	AICard('Kanav, Killer of Kidney Beans', 1400, 1800),
	AICard('Anto, the Person unable to come up with something Creative', 2300, 1000),
	TACard('Cooper, Keeper of Jellybean', 1100, 1900),
	AICard('Jin, Squirrel Overlord', 1900, 1300),
	TutorCard('Dorothea Douvos Tsimboukeli, Ministry of Greek Foreign Affairs', 2300, 1000),
	TutorCard('Bryce, Circle Annihilator', 1100, 2100),
	InstructorCard('Pamela Fox, Your Higher-Order Highness', 0, 10000)
]

standard_deck = Deck(standard_cards)
player_deck = standard_deck.copy()
opponent_deck = standard_deck.copy()
