import credit_card_validity

credit_card = ["4", "3", "8", "8", "5", "7", "6", "0", "1", "8", "4", "1", "0", "7", "0", "7"]
print(f"""
          *****************************************************
          ***Credit Card Validity Status {credit_card_validity.credit_card_validate(credit_card)}
          ***Credit card length: {len(credit_card)}
          ***Credit Card Type: {credit_card_validity.credit_card_number(credit_card)}
          *****************************************************
""")
