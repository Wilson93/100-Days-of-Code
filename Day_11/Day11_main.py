import random
import art
print(art.logo)


player_hand =[]
dealer_hand = []

def hands():
    print(f"Dealers Hand:{dealer_hand} = {sum(dealer_hand)}")
    print(f"Players hand:{player_hand} = {sum(player_hand)}")

#cards = [11, 11] #Test hands
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def dealer():
    dealer_hand.append(random.choice(cards))
    while sum(dealer_hand) > 21 and 11 in dealer_hand:
        index = dealer_hand.index(11)
        dealer_hand[index] = 1
    while sum(dealer_hand) < 17:
        dealer()
    if (sum(dealer_hand)) > 21:
        print(f"Dealer busts you win!!!")
        hands()
        exit()
    return dealer_hand


def player():
    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    hands()
    stand = False
    while not stand:
        while sum(player_hand) > 21 and 11 in player_hand:
            index = player_hand.index(11)
            player_hand[index] = 1
            print(f"Ace dropped to 1:{player_hand}")
        if sum(player_hand) <= 21:
            hit = input("Hit or stand?:").lower().strip()
            if hit == "hit":
                player_hand.append(random.choice(cards))
                hands()
                continue
            elif hit == "stand":
                stand = True
                dealer()
        return player_hand

def black_jack():
    dealer_hand.append(random.choice(cards))
    player()
    if sum(player_hand) > 21:
        hands()
        print("Player bust!!!!")
    elif sum(player_hand) > sum(dealer_hand):
        hands()
        print("You Win !!!!")
    else:
        hands()
        print("You loose!!! better luck next time!!!")

black_jack()



#testing
# print(ace_card())
# print(dealer())
# print(len(dealer_hand))

#notes
# blackjack/21 largest number not over 21 wins anything over is bust
# 2-10 facevalue jack queen and king count as 10
# Ace can either count as either 1 or 11
# if tie = draw if dealer hand <17 dealer must draw another card
# cards = 4 10's 1-9 and ace'
