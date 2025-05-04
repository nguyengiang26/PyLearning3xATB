username = ["admin", "user1", "user2"]

'''OUTPUT:
["nam123@gmail.com", "linh456@gmail.com", "hoa789@gmail.com"]
'''

# C1
# email_list = []
# for i in username:
#     email_list.append(i + "@gmail.com")

# print(email_list)

# C2
email = map(lambda x: x + "@gmail.com",username)
print(list(email))