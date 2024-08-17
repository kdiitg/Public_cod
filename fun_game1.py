import random

l_org = []
l3 = []
# l2 = []
for i in range (25):
    l_org.append(random.randint(101, 949))


# print(l_org)
# print(len(l_org))
l_set = [*set(l_org)]
# l_set = [662, 789, 546, 552, 942, 896, 264, 402, 914, 146, 947, 564, 828, 835, 841, 999]
l_set = ["🐶", "😂", "🌵", "💯", "🎁","😡", "🧲", "🏆", "🎹", "🍔","❤️", "💻", "☎️", "⏰", "✨"]
basic_emojis = ["😀", "😂", "😍", "😎", "😢", "😡", "🤔", "😇", "🤗", "😴", "🙃", "😛"]

people_emojis = ["🥰", "🤩", "🥺", "🤷‍♀️", "🤷‍♂️", "👩‍🍳", "👩‍🏫", "👩‍🎤", "👩‍🚀", "👩‍⚕️", "👩‍🌾", "👩‍💻", "👪"]

animals_nature_emojis = ["🐶", "🐱", "🐭", "🐹", "🐨", "🦁", "🐒", "🐢", "🌳", "🌵", "🌻", "🌊"]

food_drink_emojis = ["🍕", "🍔", "🍟", "🌮", "🍣", "🍩", "🍦", "🍻", "🍷", "☕️"]

activities_emojis = ["⚽️", "🏀", "🏸", "🎮", "🎹", "🎥", "🎨", "🎪", "✨", "🎉", "🎊", "💯"]

objects_emojis = ["🎁", "🛍️", "🏆", "🧰", "🧲", "💡", "⏰", "🎤", "🎧", "☎️", "💻", "📚"]

symbols_emojis = ["❤️", "💖", "✨", "👍", "👎", "✊", "✌️", "🤝", "🙏", "❓", "❗️"]

# Shuffle the list
random.shuffle(l_set)
# l2 is a list 
# print(l_set)

l1 = l_set[0:5]
l2 = l_set[5:10]
l3 = l_set[10:15]
print(f"Row 1 is {l1}")
print(f"Row 2 is {l2}")
print(f"Row 3 is {l3}")

def suffel(new_arr):
    global l1, l2,l3
    # print(new_arr)
    l1 = new_arr[0:15:3]
    l2 = new_arr[1:15:3]
    l3 = new_arr[2:15:3]
    print(f"Row 1 is {l1}")
    print(f"Row 2 is {l2}")
    print(f"Row 3 is {l3}")

    return l1, l2, l3


# which set consist the num
def runfn():
    global l1, l2, l3
    for i in range(3):
        set_num = int(input("Enter in which set ur num is ->"))

        if set_num == 1:
            # new_arr = [*l2, *f'l1', *l3]
            new_arr = [*l3, *l1, *l2]
            # print(new_arr)
            suffel(new_arr)
        elif set_num == 2:
            new_arr = [*l1, *l2, *l3]
            # print(new_arr)
            suffel(new_arr)
        else:
            new_arr = [*l2, *l3, *l1]
            # print(new_arr)
            suffel(new_arr)
    
    # new_arr = [*l1, *l3, *l2]
    # suffel(new_arr)
    print("***************")
    print(f"you are think about this {new_arr[7]}")

runfn()

