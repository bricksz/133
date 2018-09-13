import random
import functions as f

def count_card(hand,face,suit):
    face_ix = 0
    suit_ix = 0
    for x in hand:
        if face in x:
            face_ix += 1
        if suit in x:
            suit_ix += 1
    return hand, face_ix, suit_ix
face = 'Ace'
suit = 'Clover'

hand_detailed = count_card(f.deal(),face,suit)
print(hand_detailed[0],
      "\n number of {}(s): ".format(face), hand_detailed[1],
      "\n number of {}(s): ".format(suit), hand_detailed[2])
      
