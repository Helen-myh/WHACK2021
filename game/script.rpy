# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Y = Character("You", color='#3366CC')
define T = Character("Teacher", color='#8D539A')
define A = Character("International Advisor", color='#2A7FBA')
define R = Character("Roommate", color='#2A7FBA')




# The game starts here.

label start:
    play music "audio/bgm_happy_upbeat.mp3" volume 0.15

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

    
    

    label accepted():

        "you have been accepted to your {color=#D10E33}Dream college{/color}."

        Y "OMG! I got in! I'm gonna spend my next four years in a whole new country!"

    scene bg computer
    with fade

    menu where_to_live:
        "You are moving away, where do you want to live in your new city?"
        "On Campus":
            $ money -= 0.5
            $ social += 1
            "You email Campus living to look into dorm room assignment."
            menu select_roommate_oncampus: 
                "Which roommate would you like to choose?"
                "A social roommate":
                    $ social += 1
                    jump packing
                "A studious roommate":
                    $ academic += 1
                    jump packing
                "A good listener":
                    $ health += 1
                    jump packing
                #"Random":

    
        "Off Campus":
            "You look online for an apartment"
            menu housing_options:
                "Which of these two options will you pick?"
                "Closer but more expensive":
                    $ social += 0.5
                    $ money -= 1
                    jump select_roommate_offcampus
                "Further but cheaper":
                    $ farOffCampus = True
                    jump select_roommate_offcampus

            label select_roommate_offcampus():

            menu select_roommate_offcampus_boolean: 
                "Would you like to look for a roommate or not?"
                "Yes":
                    $ money += 0.5
                    
                    menu select_roommate_offcampus_choices: 
                        "What kind of roommate are you looking for?"
                        "A social roommate":
                            $ social += 1
                            jump packing
                        "A studious roommate":
                            $ academic += 1
                            jump packing
                        "A good listener":
                            $ health += 1
                            jump packing
                "No":
                    $ money -= 0.5
                    jump packing


    label packing():
    
    "Now that you know where your're going to stay, let's focus on what you're going to take to school."
    
    Y "The airline only allow 70 pounds. How heavy is that even?"
    "You googled online and found that it's about 32kg."

    Y "I'll need all my documents with me."
    
    scene bg checklist
    with fade

    Y "Here's my Passport and my visa, I-20, college acceptance letter, vaccination records. What else? Right, probably my high school transcript as well."
    "You picked up your documents."
    $ weight -= 0.25
    "You have [weight] kilos left."
    
    scene bg suitcase
    with fade

    menu packing2:
        
        Y "How many clothes should I pack..."
        "Shoes and clothes for a few weeks":
            $ weight -= 1.5
        "Some summer clothes plus winter clothes":
            $ weight -= 4
        "Pack as much as I can!":
            $ weight -= 15

    menu packing3:
        Y "Do I bring my laptop with me or should I buy a new one?"
        "Bring your old laptop (don't forget your charger)":
            $ weight -= 2
        "Buy a new one when I get there":
            $ money -= 0.5
    
    "Wow, I haven't packed everything else yet and I only have [weight] kilos left?"


scene bg airplane 
with fade
play sound "audio/airplane.mp3" volume 0.20
 
"A few weeks pass. You make it safe to campus. You successfully go through the orientation process and the first week of classes!"

scene bg campus
with fade

"It is Friday and you hear from a colleague that there will be a social gathering in some student housing on campus."
if farOffCampus == True:
    Y "Oh no! The bus'll probably stop running by the time I get back."
    "You didn't go to the party."
    menu home_choices:
        "You go back home. Would you like to"
        "Go back to your room and work on some documents your international advisor provided you earlier today":
            scene bg dorm
            with fade
            $ workOpportunity = True
        "Call back home and catch up with your family":
            scene bg phonecall
            with fade
            $ health += 1

else:
    menu friday_choices:
        "What do you do?"
        "LET'S PARTYYY!":
            scene bg social
            with fade
            $ social += 1
        "Stay in the library to study and get ahead on your school work":
            scene bg classroom
            with fade
            $ academic += 1
        "Go back to your room and work on some documents your international advisor provided you earlier today":
            scene bg dorm
            with fade
            $ workOpportunity = True
        "Call back home and catch up with your family":
            scene bg phonecall
            with fade
            $ health += 1

scene bg advisor
with fade
"A week later, you visit the career center as suggested by your advisor."
A "We have two on campus jobs that you might be interested in."
A "The first one is the school's blogger, which is not very time consuming and takes about 2 hr/week."
A "Or you could work as a help desk worker if you want to work for extra hours, generally 6 hr/week."


menu job_choices:
    "I think I "
    "would like to work as a blogger.":
        $ social -= 0.5
        $ academic -= 0.5
        if workOpportunity == True:
            A "Fantasic! I'll see you tomorrow then."
            $ money += 0.5
        else:
            A "Great! Did you get your social security number?"
            "You haven't got your documents settled and have to wait for several weeks before you can start to earn your payroll."
            $ money -= 0.25

    "want to be a help desk worker.":
        $ social -= 1
        $ academic -= 1
        if workOpportunity == True:
            A "Fantasic! I'll see you tomorrow then."
            $ money += 1
        else:
            A "Great! Did you get your social security number?"
            "You haven't got your documents settled and have to wait for several weeks before you can start to earn your payroll."
            $ money -= 0.5

    "would like to focus on my academics for now":
        $ social += 1
        $ academic += 1
        $ money -= 1


scene bg summer
with fade
"Time flies, and the school year is coming to an end. You are now planning for your summer."

menu internship:
    "Would you like to find an internship?"
    "Yes":
        $ internship = True
        if academic < 1:
            "Unfortunately you are a little behind on your grades and have to spend extra time talking to recruiters to get a job."
            $ extratime = True
        elif academic < 3:
            "Your hard work paid off. You have an internship lined up later this summer."
        else:
            "Your hard work paid off! You are qualified for a intership sponsered by your school this summer."
    "No":
        $ internship = False

if social >= 3:
    menu social:
        "A friend planned a trip over the first weekend of the summer and invited you to come before your internship starts! Are you going with them?"
        "Yes!":
            if (internship == True) and (extratime == True):
                "Since you need more time to get an internship, you are unable to go to the trip."
            else:
                if money < 3.5:
                    "Unfortunately, you didn't do great with your budget and can't afford the trip."
                else:
                    "You did great with your budget and deserve a break!"

        "No":
            "You decide to save your budget for your next year."

if money >= 6.5:
    "Congrats! The path you chose earns you the most saving!"
if social >= 5:
    "Congrats! You make great relations with your friends and are a real social butterfly!"
if academic >= 4:
    "Congrats! You're hard work and determination brought you academic excellence."
if health >= 3:
    "Congrats! You took great care of your self. That's always important to remember."

    # This ends the game
label end_game():
    return
