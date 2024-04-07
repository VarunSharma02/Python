card=int(input("Enter the card's expiration month"))
card_type=input("Enter the card type (Mastercard or visa):").lower()
if(card >=1 and card <=12) and (card_type=="mastercard" or card_type=="visa"):
    print("Credit card is valid.")
else:
    print("Credit card is not valid.")