career_options ="""
1. Doctor
2. Engineer
3. Pilot
4. Marine
5. Influencer
"""
print(career_options)
for future_option in career_options:
    future_option = input("Please select any option from the list:")
    print(future_option)
    if future_option in career_options:
        print("May you succeed in life")
        break
    elif future_option == "quit":
        print("Please find a life goal")
        break
    else:
        print("Please select from the list given")
        print(career_options)
