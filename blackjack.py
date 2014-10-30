# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
deck = []
dealer = []
player = []
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0

    def __str__(self):
        string = "The hand contains "
        for card in self.hand:
            string  = string +  card.suit + card.rank + " "
        return string

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        self.value = 0
        for val in self.hand:
            self.value += VALUES[val.get_rank()]
        
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        
        aux = [val.get_rank() for val in self.hand]
        if RANKS[0] in aux:
            if self.value + 10 <= 21:
                self.value = self.value + 10
                
        return self.value
        
   
    def draw(self, canvas, pos):
        if len(self.hand) < 5:
            max_hand = len(self.hand)
        else:
            max_hand = 5

        for i in range(max_hand):
            self.hand[i].draw(canvas, [pos[0] + (CARD_SIZE[0] + 20) * i, pos[1]])

 
    
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                val = ""
                self.deck.append(val + suit + rank)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        val = Card(card[0],card[1])
        return val
    
    def __str__(self):
        string = "The deck "
        for card in self.deck:
            string = string + card + " "
        return string



#define event handlers for buttons
def deal():
    global outcome, amount, in_play, deck, dealer, player, in_play, score
    
    if in_play :
        outcome = "You lost. New deal?"
        score = score - 1
    else :
        deck = Deck()
        deck.shuffle()
    
        dealer = Hand()
        dealer.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
    
        player = Hand()
        player.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
    
        print "Player hand : " + str(player)
        print "Dealer hand : " + str(dealer)
           
        outcome = "Hit or Stand?"
        in_play = True
    

def hit():
    global deck, player, outcome
    
    if player.get_value() <= 21:
        player.add_card(deck.deal_card())
        if player.get_value() > 21:
            outcome = "You have busted."
            score = score - 1
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global player, deck, dealer, outcome, in_play
    
    if in_play:
        in_play = False
        if player.get_value() > 21:
            outcome =  "You have busted. New deal?"
            score = score - 1
        else:
            while dealer.get_value() < 17:
                dealer.add_card(deck.deal_card())
            
        if dealer.get_value() > 21 :
            outcome = "Dealer has busted. You win! New deal?"
            score = score + 1
        else :
            if player.get_value() <= dealer.get_value() : 
                outcome = "Dealer wins! New deal?"
                score = score - 1
            else :
                outcome = "You win! New deal?"
                score = score + 1
        
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global dealer, player, outcome
    
    canvas.draw_text('Blackjack', (80, 40), 40, 'Blue')
    canvas.draw_text("score : " + str(score), (400, 40), 40, 'White')
    
    dealer_text = 'Dealer'
    if not in_play:
        dealer_text += ' (' + str(dealer.get_value()) + ')'
    canvas.draw_text(dealer_text, (80, 100), 30, 'Black')
    dealer.draw(canvas, [80,150])
    
    dealer_text = 'Player'
    if not in_play:
        dealer_text += ' (' + str(player.get_value()) + ')'
    canvas.draw_text(dealer_text, (80, 350), 30, 'Black')
    player.draw(canvas, [80,400])
    
    canvas.draw_text(outcome, (80, 580), 40, 'White')
    
    if in_play:
        card_loc = (CARD_BACK_CENTER[0] + CARD_BACK_SIZE[0], 
                    CARD_BACK_CENTER[1] + CARD_BACK_SIZE[1])
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                          [80 + CARD_BACK_CENTER[0], 150 + CARD_BACK_CENTER[1]],
                          CARD_BACK_SIZE)



# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric