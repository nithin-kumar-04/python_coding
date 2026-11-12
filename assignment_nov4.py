one_regular = 150
one_premium = 250


def ticket_booking():

    ticket = input("Which type of ticket would you like to book? ")

    print(f"You have selected: {ticket}")

    ticket_types = ["regular", "premium"]

    if ticket in ticket_types:

        if ticket == "regular":

            how_many = int(input("How many regular tickets would you like to book? "))

            total_price = how_many * one_regular

            print(f"The total price of {how_many} {ticket} ticket(s) is: {total_price}")

            generate_bill = input("Would you like to generate a bill? (yes/no): ")

            if generate_bill== "yes":

                print(f"Generating bill for {how_many} {ticket} ticket(s) with total price: {total_price}")

                with open("ticket_bill.txt", "a") as f:
                    f.write(f"Bill for {how_many} {ticket} ticket(s): {total_price}\n")

        elif ticket == "premium":

            how_many = int(input("How many premium tickets would you like to book? "))

            total_price = how_many * one_premium

            print(f"The total price of {how_many} {ticket} ticket(s) is: {total_price}")

            generate_bill = input("Would you like to generate a bill? (yes/no): ")

            if generate_bill == "yes":

                print(f"Generating bill for {how_many} {ticket} ticket(s) with total price: {total_price}")

                with open("ticket_bill.txt", "a") as f:
                    f.write(f"Bill for {how_many} {ticket} ticket(s): {total_price}\n")

    else:
        print("Sorry, this type of ticket is not available.")


ticket_booking()