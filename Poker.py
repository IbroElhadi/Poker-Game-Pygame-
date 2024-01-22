import pygame
import os
import random
import math


pygame.init()#intilaise pygame 

screen_width, screen_height = 800, 600#init screen dimensions
screen = pygame.display.set_mode((screen_width, screen_height))#create window
pygame.display.set_caption("Poker Game")#window caption

background = pygame.image.load(os.path.join("Assets", "PokerTable.png"))#load background image linked from Assets
background = pygame.transform.scale(background, (screen_width, screen_height))#resize background image to the dimesnions of the window

#function to lopad card image with a paremeter
def load_cards(card_value):
    card_image = pygame.image.load(os.path.join("Assets", "card_" + card_value + ".png"))#load card using assets with parameter as the vaklue of the card
    return pygame.transform.scale(card_image, (card_width, card_height))#scale and resize card 

#function to create card
def create_card(value, position):
    return {"value": value, "position": position}#returns value and position of new card object 

def flip_card(opponent_cards):
    # Load the image of the back of the playing card
    card_back = load_cards("back")

    # Iterate through each card in the opponent's hand
    for card_obj in opponent_cards:
        x, y = card_obj["position"]
        width, height = card_width, card_height

        # Gradually decrease the width of the card (flip animation)
        for angle in range(180, 90, -2):
            # Clear the screen with the scaled background
            screen.blit(scaled_background, (0, 0))

            # Display other cards (including player and opponent cards)
            for other_card_obj in player_cards + opponent_cards:
                # Exclude the card currently being flipped
                if other_card_obj != card_obj:
                    # Load and display other cards on the screen to be revealed
                    other_card = load_cards(other_card_obj["value"])
                    screen.blit(other_card, other_card_obj["position"])

            # Calculate the scaled width based on the absolute value cosine of the angle
            scale_factor = abs(math.cos(math.radians(angle)))
            scaled_width = int(card_width * scale_factor)

            # Display the shrinking card with a turning effect
            card = pygame.transform.scale(card_back, (scaled_width, height))
            screen.blit(card, (x, y))

            # Update the display (not flipping, but updating the screen)
            pygame.display.update()
            
            # Introduce a delay between flips for smooth animation
            pygame.time.delay(10)

        # Quickly clear the 'back' card from the display after revealing the new card
        screen.blit(scaled_background, (0, 0))
        for other_card_obj in player_cards + opponent_cards:
            # Exclude the card currently being flipped
            if other_card_obj != card_obj:
                # Load and display other cards on the screen
                other_card = load_cards(other_card_obj["value"])
                screen.blit(other_card, other_card_obj["position"])
        # Update the display (not flipping, but updating the screen)
        pygame.display.update()

        # Create new cards with increasing width (flip back animation)
        card_obj["value"] = random.choice(cards)
        for angle in range(90, 180, 2):
            # Clear the screen with the scaled background
            screen.blit(scaled_background, (0, 0))

            # Display other cards
            for other_card_obj in player_cards + opponent_cards:
                # Load and display other cards on the screen
                other_card = load_cards(other_card_obj["value"])
                screen.blit(other_card, other_card_obj["position"])

            # Calculate the scaled width based on the cosine of the angle
            scale_factor = abs(math.cos(math.radians(angle)))
            scaled_width = int(card_width * scale_factor)

            # Update the display (not flipping, but updating the screen)
            pygame.display.update()
            
            # Introduce a delay for smooth animation
            pygame.time.delay(5)


cards = ["spades_A", "hearts_A", "diamonds_A", "clubs_A",
         "spades_02", "hearts_02", "diamonds_02", "clubs_02",
         "spades_03", "hearts_03", "diamonds_03", "clubs_03",
         "spades_04", "hearts_04", "diamonds_04", "clubs_04",
         "spades_05", "hearts_05", "diamonds_05", "clubs_05",
         "spades_06", "hearts_06", "diamonds_06", "clubs_06",
         "spades_07", "hearts_07", "diamonds_07", "clubs_07",
         "spades_08", "hearts_08", "diamonds_08", "clubs_08",
         "spades_09", "hearts_09", "diamonds_09", "clubs_09",
         "spades_10", "hearts_10", "diamonds_10", "clubs_10",
         "spades_J", "hearts_J", "diamonds_J", "clubs_J",
         "spades_K", "hearts_K", "diamonds_K", "clubs_K",
         "spades_Q", "hearts_Q", "diamonds_Q", "clubs_Q"] #initialises all card options

card_width, card_height = 50, 75 #inits card dimensions

positions = [#inits positions cards should go to 
    (250, 100), (300, 100), (350, 100),(400, 100), (450, 100),(250, 400), (300, 400), (350, 400), (400, 400), (450, 400)
]

opponent_positions = [ #inits positions of only opponent cards (used to diffreniate between the two for flipping 
    (250, 100), (300, 100), (350, 100),(400, 100), (450, 100)]

opponent_cards = []# init list of opponent cards
player_cards = []#init list of players cards

#function used to determine the winner before ending a gamme
def determine_winner(player_cards, opponent_cards):
    player_rank = evaluate_hand(player_cards)#the players rank(what their hand means) is initialised by calling evaluate hand function with players card
    opponent_rank = evaluate_hand(opponent_cards)#same thing as player rank but for opponent

    return player_rank, opponent_rank#returns the ranks to be used for letting the player know whats going on
def evaluate_hand(cards):
    # Map cards to values (2-14)
    values = [get_card_value(card["value"]) for card in cards]
    value_counts = {value: values.count(value) for value in set(values)}

    # Check for Royal Flush
    if all(value in values for value in [10, 11, 12, 13, 14]) and len(set(card["value"][:-1] for card in cards)) == 1:
# Verifies if all values are present in the set [10, 11, 12, 13, 14]
# Checks if all cards belong to the same suit.
        return "Royal Flush"

    # Check for Straight Flush
    if any(value_counts.get(value, 0) >= 5 for value in range(2, 11)):
# Checks if there are at least five consecutive values in the cards.
# The `value_counts.get(value, 0)` retrieves the count of a value, and 0 is used as a default if the value is not present.
        return "Straight Flush"

    # Check for Four of a Kind
    if 4 in value_counts.values():
# Verifies if there is a value with a count of 4.
        return "Four of a Kind"

    # Check for Full House
    if 3 in value_counts.values() and 2 in value_counts.values():
#Checks if there is a value with a count of 3 and another with a count of 2.
        return "Full House"

    # Check for Flush
    if len(set(card["value"][:-1] for card in cards)) == 1:
# Verifies if all cards belong to the same suit.
        return "Flush"

    # Check for Two Pair
    if list(value_counts.values()).count(2) == 4:
# Checks if there are 2 vlues with a count of 2 or a value with a count of 4
        return "Two Pair"

    # Check for One Pair
    if 2 in value_counts.values():
# Checks if there is a vlue with a count of 2
        return "One Pair"

    # High Card if none of the above
    return "High Card"

def get_card_value(card_string):
    # Extract the numeric part from the card string
    numeric_part = "".join(char for char in card_string if char.isdigit())

    # Convert the numeric part to an integer
    if numeric_part:
        return int(numeric_part)
    elif card_string[-1] == "A":
        return 14  # Ace
    elif card_string[-1] in "JQK":
        return 10  # Face cards
    else:
        return 0  # Default value for invalid cases

scaled_background = pygame.transform.scale(background, (screen_width, screen_height)) #gets the scaled background for image loading

player_balance = 100 #how much money player starts with
opponent_balance = 100#how much money opponent starts with
current_bet = 20#what the minimum starting bet it (standard at casinos so they can SCAM YOU)
font = pygame.font.Font(None, 30)#inits font for use with text

#iniots text to see on start or to be used later
player_ask_text = font.render("", True, (255, 255, 255))
player_choice_text = font.render("", True, (255, 255, 255))
text = font.render("PRESS SPACE TO START!", True, (255, 255, 255))
player_balance_text = font.render("Player Balance: $" + str(player_balance), True, (255, 255, 255))
opponent_balance_text = font.render("Opponent Balance: $" + str(opponent_balance), True, (255, 255, 255))
player_status_text = font.render("", True, (255, 255, 255))
opponent_status_text = font.render("", True, (255, 255, 255))

raise_amount = ""  # Variable to store the raise amount
# Initialize raise_text_box position and dimensions
raise_text_box = pygame.Rect(500, 290, 100, 30)  # Position of the raise input box

#function to show what oppionent does
def opponent_turn():
    global current_bet, player_ask_text, player_choice_text, player_balance, opponent_balance, text, player_status_text, player_balance_text, opponent_balance_text, opponent_status_text
    # Declare relevant variables as global

    #clears top corner textbox
    text = font.render(" ", True, (255, 255, 255))

    #decides what opponent does
    action = random.randint(1, 3)

    if action == 1:
        # Fold
        flip_card(opponent_cards)
        
        player_ask_text = font.render("", True, (255, 255, 255))#clears text
        player_choice_text = font.render("Opponent Folded. You win!", True, (255, 255, 255)) #tell p[layer opponent folded and player won]
        player_balance += current_bet#upodates players balance
        opponent_balance -= current_bet#upodates opponents balance
        player_balance_text = font.render("Player Balance: $" + str(player_balance), True, (255, 255, 255))#upodates players balance text to show in window
        opponent_balance_text = font.render("Opponent Balance: $" + str(opponent_balance), True, (255, 255, 255))#upodates opponents balance text to show in window
    elif action == 2:
        # Call
        flip_card(opponent_cards) #flips card revelaing opponents hand
        player_rank, opponent_rank = determine_winner(player_cards, opponent_cards) #determines who won the game
        player_choice_text = font.render("Opponent Called on $" + str(current_bet), True, (255, 255, 255))#lets player know why game ended
        player_ask_text = font.render("", True, (255, 255, 255))#clears text
        player_status_text = font.render(player_rank, True, (255, 255, 255))#shos what player hand was indfront of player
        opponent_status_text = font.render(opponent_rank, True, (255, 255, 255))#shows what opponent hand means infront of player
        #tells the player tghe result of the game in addition to updating the balance
        if player_rank == opponent_rank:
            player_choice_text = font.render("Its a tie! The pot is split!", True, (255, 255, 255))
            player_balance += current_bet / 2
            opponent_balance += current_bet / 2
        elif player_rank > opponent_rank:
            player_choice_text = font.render("Player WINS!", True, (255, 255, 255))
            player_balance += current_bet
            opponent_balance -= current_bet
        else:
            player_choice_text = font.render("Opponent Wins!", True, (255, 255, 255))
            player_balance -= current_bet
            opponent_balance += current_bet
    elif action == 3:
        # Raise
        raise_amount_opponent = random.randint(1, 100)
        current_bet += raise_amount_opponent
        player_ask_text = font.render("", True, (255, 255, 255))
        player_choice_text = font.render(f"Opponent raised by ${raise_amount_opponent}!", True, (255, 255, 255))
        text = font.render("Press Space to continue", True, (255, 255, 255))#since opponent raises player has to click space to continue playing restarting the choosing cycle

    player_balance_text = font.render("Player Balance: $" + str(player_balance), True, (255, 255, 255))
    opponent_balance_text = font.render("Opponent Balance: $" + str(opponent_balance), True, (255, 255, 255))


# animate_cards = None #sets that cards have not moved to their desired position
deal_cards = None #sets that cards havent moved to their desirtred positon
distance = 100#sets distnace used for card travel
speed = 4#sets speed cards move at

#creates opponent and player cards for use when dealing
opponent_cards = [create_card("back", (530, 200)) for _ in range(5)]
player_cards = [create_card(random.choice(cards), (530, 200)) for _ in range(5)]

clock = pygame.time.Clock() #inits clock like FPS

running = True#lets pygamne klnow that code is running and not to end window
game_start = False#shows that game hasnt started yet (player hasnt oressed space)
raise_active = False#for use when player decides to raise to load raise menu

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #so player can shut down pygame
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: #if player presses spaqce
                screen.blit(text, (10, 10)) #reloads text ensuring its up to date
                text = font.render("Current bet is $" + str(current_bet), True, (255, 255, 255)) #shows wat current bet is
                player_choice_text = font.render(" ", True, (255, 255, 255)) #clears text
                deal_cards = opponent_cards + player_cards#deals player and opponents cards
                text = font.render("Current bet is $" + str(current_bet), True, (255, 255, 255)) #updates current bet 
                player_ask_text = font.render("Do you want to fold (F), call (C), or raise (R)? ", True, (255, 255, 255))#asks player for their game decision
                game_start = True#shows that game has started
            elif event.key == pygame.K_f:#fold(give up)
                if game_start:
                    flip_card(opponent_cards)#reveales opponent hand
                    player_ask_text = font.render("", True, (255, 255, 255))#clears text
                    player_choice_text = font.render("You Folded and lost!", True, (255, 255, 255))#tells player result
                    player_balance -= current_bet#updates balance
                    opponent_balance += current_bet#updates balance
                    player_balance_text = font.render("Player Balance: $" + str(player_balance), True, (255, 255, 255))#updates balance text
                    opponent_balance_text = font.render("Opponent Balance: $" + str(opponent_balance), True, (255, 255, 255))#updates balance text
            elif event.key == pygame.K_c:#call (end game )
                if game_start:
                    flip_card(opponent_cards)#flips cards revealing opponent hand
                    player_rank, opponent_rank = determine_winner(player_cards, opponent_cards) #determines who had the better cards
                    game_start = False #shows gtame has ended
                    text = font.render("You Called on $" + str(current_bet), True, (255, 255, 255))#shows what the current bet is when playert called
                    player_ask_text = font.render("", True, (255, 255, 255))#clears text
                    player_status_text = font.render(player_rank, True, (255, 255, 255))#shows player hand ranking
                    opponent_status_text = font.render(opponent_rank, True, (255, 255, 255))#shows opponent hand ranking

                    #updates text and balance depending in outcome
                    if player_rank == opponent_rank:
                        player_choice_text = font.render("Its a tie! The pot is split!", True, (255, 255, 255))
                        player_balance += current_bet / 2
                        opponent_balance += current_bet / 2
                    elif player_rank > opponent_rank:
                        player_choice_text = font.render("Player WINS!", True, (255, 255, 255))
                        player_balance += current_bet
                        opponent_balance -= current_bet
                    else:
                        player_choice_text = font.render("Opponent Wins!", True, (255, 255, 255))
                        player_balance -= current_bet
                        opponent_balance += current_bet
                    player_balance_text = font.render("Player Balance: $" + str(player_balance), True, (255, 255, 255))
                    opponent_balance_text = font.render("Opponent Balance: $" + str(opponent_balance), True, (255, 255, 255))
            elif event.key == pygame.K_r:#raise (I am confident and want to bet more)
                if game_start:#ensures game has started when running this
                    player_ask_text = font.render("Enter raise amount:", True, (255, 255, 255))#asks player to enter ement
                    text = font.render("Press Enter to input raise.", True, (255, 255, 255))#tells player what to do
                    raise_active = True#Switches raise active to let code know to laod input box
            elif event.key in (pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9):
                raise_amount += event.unicode#monitors number presses for use as the players input
            elif event.key == pygame.K_BACKSPACE:#allows player to delete and change the number
                if raise_active:
                    raise_amount = raise_amount[:-1]#substrracts the one closest to the left
            elif event.key == pygame.K_RETURN:#if player inputs the code
                if raise_active:#ensures raise is active for this so player dosnt change this early(excedption handeling)
                    raise_amount_int = int(raise_amount)#updates the raise amount
                    current_bet += raise_amount_int#updates what the cuirren t bet is
                    player_ask_text = font.render("", True, (255, 255, 255))#clears text
                    player_choice_text = font.render(f"You raised by ${raise_amount_int}!", True, (255, 255, 255))#shows player rases by how much
                    raise_amount = ""  # Reset raise amount after processing
                    raise_active = False#shows raise has ended

                    pygame.time.delay(40) #player waits for 40 ticks (40/60th of a second
                    opponent_turn()

    screen.blit(scaled_background, (0, 0))#for loading the vbackground image at posirtion 0,0

    #function for loading cards
    for card_obj in player_cards + opponent_cards: #for cards loop
        card = load_cards(card_obj["value"])#loads card with the desired value
        x_position, y_position = card_obj["position"]#sets cards to desired start position
        screen.blit(card, (x_position, y_position))#updates screen by laoding cards at desires position

    #loads images for use to imiitate a stack of cards (its fake just like in real casinos)
    card_back = load_cards("back")
    screen.blit(card_back, (525, 200))
    card_back = load_cards("back")
    screen.blit(card_back, (530, 200))
    card_back = load_cards("back")
    screen.blit(card_back, (535, 200))

    #updates all textx 
    screen.blit(text, (10, 10))
    screen.blit(player_ask_text, (180, 300))
    screen.blit(player_status_text, (290, 380))
    screen.blit(opponent_status_text, (290, 180))
    screen.blit(player_choice_text, (290, 290))
    screen.blit(player_balance_text, (10, 530))
    screen.blit(opponent_balance_text, (500, 10))

    #checxks if player has chosen to raise 
    if raise_active:
        pygame.draw.rect(screen, (255, 255, 255), raise_text_box, 2)#loads text box for input
        surf = font.render(raise_amount, True, (255, 255, 255))#shows what the player has input thus far
        screen.blit(surf, (raise_text_box.x + 5, raise_text_box.y + 5))#loads what player has input


    #     # Card animation
    # if animate_cards:
    #     for card_obj in animate_cards:
    #         x, y = card_obj["position"]
    #         target_x, target_y = 530, 200  # Final position
    #         direction_x = (target_x - x) / animation_distance
    #         direction_y = (target_y - y) / animation_distance

    #         # Move towards the final position
    #         card_obj["position"] = (x + direction_x * animation_speed, y + direction_y * animation_speed)

    #     # Check if all cards are close to the final position
    #     if all(
    #         abs(card_obj["position"][0] - target_x) <= animation_speed
    #         and abs(card_obj["position"][1] - target_y) <= animation_speed
    #         for card_obj in animate_cards
    #     ):
    #         animate_cards = []  # Stop animation

    #if its time to deal cards
    if deal_cards:
        # Iterate over each card object in the list of dealt cards
        for card_obj in deal_cards:
            # Extract current position (x, y) of the card
            x, y = card_obj["position"]

            # Get the index of the card in the deal_cards list
            index = deal_cards.index(card_obj)

            # Check if the index is within the range of the positions list
            if 0 <= index < len(positions):
                # Retrieve the target position (target_x, target_y) for the card
                target_x, target_y = positions[index]

                # Calculate the direction components for moving towards the target position
                direction_x = (target_x - x) / distance
                direction_y = (target_y - y) / distance

                # Update the card's position based on the direction components and speed
                card_obj["position"] = (x + direction_x * speed, y + direction_y * speed)


    pygame.display.flip()#uopdates image
    clock.tick(60)#this many times a second

pygame.quit()#once everything is done quit window
