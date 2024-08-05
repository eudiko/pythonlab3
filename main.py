import smartscan_registration_module as scan

user_data = []

print("***Enter the user data***")

choice = True
i = 1
while choice:
    print("User ", i)
    name = input("Enter name: ")
    email = input("Enter email: ")
    data = f"{name},{email}"
    user_data.append(data)
    more = input("Do you want to add another user? (yes/no): ")
    if more.lower() == "yes":
        i += 1
    else:
        choice = False

all_user_data = "\n".join(user_data)
scan.generate_qr_code(all_user_data)

scan.RegisterUserFromScan("img_code.png")