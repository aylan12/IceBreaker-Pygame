# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg park = "Park1.jpeg"
image SpookyHappy = "UserHappy.png"
image bg party = "the_jp_mansion_night.jpg"
image bg inside = "nightstreet.jpeg"
define s = Character('Spooky', color="#f11d0e" )


# The game starts here.


label start:
scene bg park
show SpookyHappy
"Spooky" "Boo! Happy Halloween!"
"Spooky" "This is the best time of the year!"


label sprites:
show SpookyHappy
"Spooky" "I'm throwing a Halloween party. Will you help?"
"Spooky" "Yay! Let's go to the party venue!"
show bg party
with fade

scene bg party
show SpookyHappy with moveinleft
"Spooky" "Here it is! Cute right?"
"Spooky" "Oh shoot! I forgot I never got decorations!"
"Spooky" "Will you play this minigame to help earn decorations?"

scene bg inside
show SpookyHappy with moveinright
"Spooky" "Awesome job! This party looks great!"
"Spooky" "Now go enjoy yourself!"
"Spooky" "Thanks for helping make this party a success"




