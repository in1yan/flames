

def flames(UserName_1, UserName_2):
    UserName_1 = UserName_1.lower().replace(" ", "")
    UserName_2 = UserName_2.lower().replace(" ","")
    if UserName_1 != UserName_2:
        for i in UserName_1:                            
            for n in UserName_2:
                if i==n:
                    UserName_1 = UserName_1.replace(i, "", 1)
                    UserName_2 = UserName_2.replace(n, "", 1)
                    break
        count = len( UserName_1 + UserName_2 )
        if count > 1:
            list1 = ["Friends 😄😄", "Lovers ❤❤", "Affection 🧲🧲", "Marriage 👰🤵💐 ", "Enemy 😈😈", "Siblings 👯👥🧑‍🤝‍🧑"]
            while len(list1) > 1:
                c = count % len(list1)
                s_index = c-1
                if s_index >=0:
                    left = list1[:s_index]
                    right = list1[s_index+1:]
                    list1 = right + left 
                else:
                    list1 = list1[:len(list1)-1]
            return list1[0]

if __name__ == "__main__":
    UserName_1 = input("enter your name: ")
    UserName_2 = input("enter your crush name: ")
    print("Relationship status is " + str(flames(UserName_1=UserName_1, UserName_2=UserName_2)))
