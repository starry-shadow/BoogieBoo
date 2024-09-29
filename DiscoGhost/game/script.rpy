# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Ghost")


# The game starts here.


transform items:
    xalign 0.5
    yalign 0.5

label start:
    call screen dressup


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Welcome to Disco Ghost Dress up"

    e "You can toggle the clothes to dress up the disco ghost"

    # This ends the game.

    return
