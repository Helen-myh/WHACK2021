# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Y = Character("You", color='#3366CC')
define T = Character("Teacher", color='#8D539A')
define A = Character("International Advisor", color='#2A7FBA')
define R = Character("Roommate", color='#2A7FBA')




# The game starts here.

label start:

    call initialize_var

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg letter
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    menu open_letter:
        "You receive a letter."
        "Open letter":
            jump accepted

    
    #you have been accepted to your {color=#D10E33}Dream college{/color}."

    label accepted():

        Y "OMG! I got in! I'm gonna spend my next four years in a whole new country!"



    # This ends the game.

    return
