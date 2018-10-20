# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image CL icon1 = "clem_uh.png"
image JO icon2 = "joel_dontknow.png"
image MI icon3 = "meirzwiak.png"


define CL = Character("CLEMENTINE", image = "CL", who_color="#FF4500", what_color = "#333333",what_prefix = '"', what_suffix='"')
define JO = Character("JOEL", image = "JO", who_color="#6B8E23", what_color = "#333333",what_prefix = '"', what_suffix='"')
define MI = Character("MIERZWIAK", image = "MI", who_color = "#999999", what_color = "#333333", what_prefix = '"', what_suffix='"')

# The game starts here.


label start:

 play music "THE_COCONUT_MONKEYROCKET_Aunt_Fish.mp3"

# Show a background. This uses a placeholder by default, but you can
# add a file (named either "bg room.png" or "bg room.jpg") to the
# images directory to show it.

 scene bg start erase

# This shows a character sprite. A placeholder is used, but you can

# replace it by adding a file named "eileen happy.png" to the images
# directory.
# These display lines of dialogue.

 ""
 show joel_dontknow
 JO "Is there any sort of risk of brain damage?"

 hide joel_dontknow
 show meirzwiak

 MI "Well, technically, the procedure itself is brain damage, but on a par with a night of heavy drinking. Nothing you'll miss."
 "(Joel looks quizzically at the eroding environment. Suddenly he gets it.)"
 
 hide meirzwiak
 show joel_dontknow

 JO "It's happening now! I'm already in my brain."
 hide joel_dontknow
 hide meirzwiak


#$ dating = renpy.random.choice(['party','bed', 'train'])

 menu:
  "Continue?":
   jump start
  "Stop it!":
   menu:
    "party":
     jump party
    "bed":
     jump bed
    "train":
     jump train

 stop music
 "THE_COCONUT_MONKEYROCKET_Aunt_Fish.mp3"
 pause 2


label party:

 play music "Aquatic_Inspiration_Dayfade.mp3"

 show bg sink_001
 JO "I love getting bathed in the sink. It's such a feeling of security."
 CL "(giggling) I've never seen you happier."
 
 menu:
  "Keep bathing?":
   jump party
  "annoying":
   show dumb-and-dumber-jim-carrey
   pause 5
   "SORRY!!"
   jump start



label bed:
 show bg two_love
 
 CL "I think. Anyway, I've tried all their colors. More than once. I'm getting too old for this. But it keeps me from having to develop an actual personality. I apply my personality in a paste. You?"
 JO "Oh, I doubt that's the case."
 CL "Well, you don't know me, so... you don't know, do you?"
 
 show joel_side_smile

 menu: 
  "Sorry. I was just trying to be nice.":
   hide joel_side_smile
   show joel_side_smile_g
   jump start
  "Yeah, I got it.":
   jump complete

label train:
 show bg inside-dutch-train-
 show clem_happy
 
 CL "Hi!"

 show joel_side_smile
 hide clem_happy
 JO "(looks over.) I'm sorry."
 
 hide joel_side_smile
 show clem_happy
 CL "Why?"

 show joel_side_smile
 hide clem_happy
 JO "Why what?"

 hide joel_side_smile
 show clem_happy
 CL "Why are you sorry? I just said hi."

 show joel_side_smile
 hide clem_happy
 JO "No, I didn't know if you were talking to me, so..."

 hide joel_side_smile
 show clem_happy
 CL "She looks around the empty car.)Really?"

 show joel_side_smile
 hide clem_happy
 JO "(embarrassed) Well, I didn't want to assume."

 hide joel_side_smile
 show clem_happy
 CL "Aw, c'mon, live dangerously. Take the leap and assume someone is talking to you in an otherwise empty car."

 show joel_side_smile
 hide clem_happy
 JO "Anyway. Sorry. Hi."

 hide joel_side_smile
 show clem_happy 
 CL "It's okay if I sit closer?"

 hide clem_happy
 show clem_happy_g
 show joel_side_smile_g 

 menu:
 
  "It's okay, really.":
   jump complete
  "No, I mean, I don't know. I can't really think of much to say probably.":
   jump complete

label complete:
 show ending_001
 "The End"

return
