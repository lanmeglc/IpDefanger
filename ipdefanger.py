def defanger(user_ip):
    new_address = ""
    split_address = user_ip.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address
input_ip = input("What ip you want to defang? ")
defanged_ip = defanger(input_ip)
print(defanged_ip)