# PROJECT TITLE
#### Video Demo: <>
#### Description:

I have always considered tracking initiative and turn order in table top roleplaying games tiresome, as well as flip through pages and pages in order to find the random table encounter I am looking for and then flip more pages in order to find the monster/monsters my players have to fight. In my app you are able to do all that with few clicks, after populate the database with all the required information that is!

In the home page of my web app you can look at all the functionality you have access, from left to right: Encounter Tables, in which you can find Randon Table Encounters and Create Table; List of Monster in which you can find Monster and Create Monster; and finally List of characters, in which you can find Character and Save Character.

I will now explain all the funcionality of each part.


## List of characters:

In order to keep track of all your player characters (PCs from now on), you have to create them (or save their info in the database). To do so you can click on "Save Character" button in the homepage or the button in the list of character.

On the other hand if you want to just see all your PCs info, click on "Character" button in the homepage.

### Save Character:

In this page you will be presented with a form with the following fields: Player, Character, Ancestry, Class, Level, Armor Class, Hit points, Passive Perception, Strength, Dexterity, Constitution, Intelligence, Wisdom and Charisma.

Player - refers to the name of the player.
Character - refers to the name of the character.
Ancestry - commonly refered to as race, refers to which of those you descend from (example: orcs, gnomes...).
Class - refers to the class of your character, in other words how your character aproaches combat.
Level - refers to the level your character is in the aforementioned class.
Armor Class - refers to the current armor class your character has, in other words, how difficult is to be hit by other in combat.
Hit Points - refers to how much damage can your character endure before falling unconcious.
Passive Perception - refers to the inherent ability your character has to sense what is hidden from you without actively doing so.
Strength, Dexterity, Constitution, Intelligence, Wisdom and Charisma - refers to the modifier you character has to add to saving throws, in other words, this is a number that you add to a 20-side dice (from now on d20) in order to not be affected or be affected less when being targeted by traps, spells or similar effects.

I have decided to just implement these stats as they are most conveninient to have around. The characters sheets have a lot more information not conveyed in this form, but I deemed this stats and information enough to be known to the Dungeon Master (from now on DM).

After you have clicked the "Save character" button you will be redirected to "Character".

### Character:

In "Character" you are able to see a list of all characters in the database neatly ordered in a single table.


## List of Monsters:

### Create Monster:

As in "Save Character" you will be presented with a form in which you can add all the relevant information a DM may want from a Monster/Enemy. The fields are: Name, Type, Challenge rating, Passive Perception, Armor Class, Hit Points, Damage Reduction, Speed, Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma, Skill 1, Skill 2, Skill 3, Action 1, Action 2, Action 3 and Spells.

Name - refers to the monster's name.
Type - refers to the monster's type of creature (undead, humanoid...) and size (small, medium, large...).
Challenge rating - refers to how difficult it is for a party of 4 PCs, for example, a Challenge Rating of 4 should be considered as a normal difficulty for a party of 4 PCs at level 4.
Passive Perception - refers to the inherent ability your character has to sense what is hidden from you without actively doing so.
Armor Class - refers to the current armor class your character has, in other words, how difficult is to be hit by other in combat.
Hit Points - refers to how much damage can your character endure before falling unconcious.
Damage reduction - refers to the inherent ability to endure certain damage types (electric, fire...) or conditions (paralyzed, frightened...).
Speed - refers to how many slots can the monster move with a single move action in squared grid.
Strength, Dexterity, Constitution, Intelligence, Wisdom and Charisma - refers to the modifier you character has to add to saving throws, in other words, this is a number that you add to a 20-side dice (from now on d20) in order to not be affected or be affected less when being targeted by traps, spells or similar effects.
Skill 1-3 - refers to non-combat specific skills the monster may have, as Keen Senses or the ability to turn invisible.
Actin 1-3 - refers to combat specific actions the monster may undertake in order to damage the PCs.
Spells - referst to the list of spells the monster may use.

When all the information is provided the user may click on "Save Monster" button so all the info can be stored in the database, and then they will be redirected to "Monster".

### Monster:

In this section you will be able to see all the main information in the database that refers to monsters. From here you can too click the button "Add New Monster" in order to access the "Create Monster" form.


## Encounter Tables:

### Create Table:

Here you will be presented with yet another form in which you can create your own random table encounter. The current setup of the form only allows you to create 18 row tables. In each row you can select the number of monster: You can choose to select only a number or a dice (which represent a range), for example "2" or "3d6", which represents "2" or a range from 3 to 18. And the last column is the monster in question, there is a dropdown from which you can choose from all the monster in the database.

There is also an input field to name your table.

When all information is provided and when the user want to proceed with this table they can click the button "Create" which will save the table and then be redirected to "Random Table Encounters".

### Random Table Encounter:

In this section you will be presented with a dropdown form, in which you can select which table to use in the encounter you players may have. When decided you may click the "Combat!" button, which will rol a number between 1 and 18 with 2 dice (1d8 and 1d12) and will pick that row of the table, it will then redirect you to the initiative screen having roled the number of monster in that row too.

### Initiative Screen:

Here you will encounter the information of the combat to come. Firstly you will see a message like this: "You are going to fight: XX"; in which XX is the number of monsters and the monster your players may have to fight.
Then you will see a form with the number of enemies, which can be changed if the DM may so choose and the monster in question, which cannot be changed.

Then, for each character in the database there will be a row with the name of that character and a field to write the initiative that needs to be provided by the players, with all the modifiers applied.

And then with all the information written in their respective field, you may push the button "Combat!"

### Encounter:

Here you will see: a button "Sort Combatants by ini", a table with all the enemies and all the characters, and below all the relevant information of the monsters.

The "Sort Combatants by ini" MUST be pushed FIRST and then it will disappear sorting the below table (enemies and characters) by their respective initiative (the app will provide automatically the correct initiative for each enemy and sort it accordingly).

Then it will appear a button "Next Turn" just below the hidden button. When pushed it will move the first row to last, so you can keep track of who is next by initiative.

In the table of enemies and characters there is all the relevant information about them and an input field to keep track of their hit points. There is too a "Delete Row" button for every row so you can remove said row for any reason (leaves the battle, dies...).

Take note that when every row moves first and put in the lower row it will change color, this is usefull to keep track of the reaction round.


## About:

Finally in the about section (access with the most right button of the navbar) you can see some of my information, background and contact information.

This is cs50.
