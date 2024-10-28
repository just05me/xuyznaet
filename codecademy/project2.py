import os
os.system('cls')
Dictionary = {
    "color":"rang",
    "hello":"salom",
    "apple":"olma",
    "foot":"oyoq",
    "ball":"to'p",
    "like":"yoqtirmoq"
}
while True:
    print("""Mini Project:Dictionary
___________________
Ingilizcha - O'zbekcha lug'at
1. Yangi so'z qo'shish
2. Lug'at ichidegi so'zlarni ko'rish
3. Izlash
4. Chiqish
___________________""")
    number = int(input("\nRaqam kiriting: "))
    if number == 1:
        newWord = input("Yangi so'z kiriting: ")
        Dictionary[newWord] = input("Tarjimasini kiriting: ")
    elif number == 2:
        print("")
        for key,value in Dictionary.items():
            print(key+" : " +value)
        print("")
    elif number == 3:
        find = input("Qidirayotkan sozingizni kiritin: ")
        found = Dictionary.get(find)
        if found:
            print(f"{find} : {found}")
        else:
            print("Bunday so'z lug'ata yoq!")
    elif number == 4:
        print("Salomat boting!")
        break






