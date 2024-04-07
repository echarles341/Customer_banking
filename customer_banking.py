# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
import create_cd_account, create_savings_account 

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("Pleae enter your saving account balance: "))
    savings_interest = float(input("please enter your interest: "))
    savings_maturity = int(input("please provide the saving for the month: "))
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'Your updated savings balance is: ${savings_interest: .2f}')
    print(f'Your updated interest earned for the month is: ${savings_maturity}')
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("Please enter your cd_balance: .2f"))
    cd_interest = float(input("Please enter your cd_interest: .2f"))
    cd_maturity = int(input("Please provide the cd maturity amount: "))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'your updated cd_interest is: .2f ')
    print(f'your updated cd_account_balance is: .2f ')
    print(f'your updated cd_maturity is: ')
    
if __name__ == "__main__":
    # Call the main function.
    main()
