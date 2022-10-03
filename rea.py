class Items:
    
    stages = ["Stage One"]

    def __init__(self, name = 'Empty', life = 5, money = 100, gold = 2, key = 0, back = False, end_game = False, have_key = 0):
        self.name = name
        self.life = life
        self.money = money
        self.gold = gold
        self.key = key
        self.back = back
        self.end_game = end_game
        self.have_key = have_key

    def check_money(self, money):
        if self.money >= money:
            self.money -= money
            return self.money
        else:
            return self.check_life(1)

    def check_life(self, life):
        if self.life < life:
            print('Your life is finish')
            self.end_game = True
            return self.end_game
        else:
            self.life -= life
            return self.life
            print('Your life has been reduce by 1 (one)')

class Interaction(Items):

    def Barman(self):
        self.check_money(5)
        interaction = """
        (Conversation With The Barman)
            you: Hey
            Barman: welcome buddy
            you: i need some drink
            Barman: soft or alcoholic?
            you: alcoholic
            Barman: you have to play a game in order to win it
            you: ok
        """
        print(interaction)

    def Dragon(self):
        print("Game in the Dungeon,")
        print("""
        You are Welcome to the SPIRIT SECTION, in this section you might have to pass an EVIL FOREST full of SpiritS. You will be given 3 things to choose from. Anything you choose is what will aid you through the Forest. (HINT: While making a choose don't choose base on NAME or STRENGTH of the Material you choose) make sure you understand before choosing any material and remember which section is this, good luck
        1. 10 different Guns
        2. A Stick full of Fire at the top
        3. A Sword
        """)

        while True:
            try:
                material = int(input("Which material do you choose? (eg. 1, 2, 3)"))
            except ValueError:
                print('please enter a number... ')
            else:
                if material == 1:
                    print("""You choose materail 1 which is 10 different Guns, but you FAILED. Remember this section is called SPIRIT SECTION, and we all know Guns can't be use to kill a spirit you lost a live""")
                    self.check_life(1)
                    break
                elif material == 2:
                    print("Hurray, finally you succeed by crossing the Forest with a Stick full of Fire, that's a nice one")
            
                    self.money += 500
                    self.gold += 100
                    try:
                        self.stage_two_levels.index("Level Two")
                    except ValueError:
                        self.stage_two_levels.append("Level Two")
                    else:
                        pass 
                    break
                elif material == 3:
                    print("You choose materail 3 which is a Sword, but you FAILED. because a sword can't kill a Spirit")
                    self.check_life(1)
                    break

    def Bar_Game(self):
        interaction = """
        (The Bar Game)
            Welcome to the Bar Game
            QUESTION: Choose a drink from the list below, that is the most acceptable in almost all occasions, this drink is not too small and the same time not too big? 
            1. Malt
            2. Coke
            3. Star
        """
        print(interaction)
        while True:
            try:
                drink = int(input("Which drink do you choose? (eg. 1, 2, 3)"))
            except ValueError:
                print('please enter a number... ')
            else:
                if drink == 1:
                    print("""You choose Malt, you win.""")
                    self.money += 500
                    self.gold += 100
                    if self.have_key == 0:
                        self.key += 1
                        self.have_key += 1
                    try:
                        self.stages.index("Stage Two")
                    except ValueError:
                        self.stages.append("Stage Two")
                    else:
                        pass 
                    break
                elif drink == 2:
                    print("You choose Coke, you lose.")
                    self.check_life(1)
                    break
                elif drink == 3:
                    print("You choose Star, you lose.")
                    self.check_life(1)
                    break

    def School_Question(self):
        interaction = """
        (The School)
            Welcome to School On this place you will be thought and after that their is just one question.
            STUDY TIME:
            me = 1
            you = 5
            me, you = you, me
            Question: what is the value of me
            1. you
            2. me
            3. none
        """
        print(interaction)
        while True:
            try:
                value = int(input("what is the value? (eg. 1, 2, 3) "))
            except ValueError:
                print('please enter a number... ')
            else:
                if value == 1:
                    print("""You choose option 1, you win.""")
                    self.money += 500
                    self.gold += 100
                    if self.have_key == 1:
                        self.key += 1
                        self.have_key += 1
                    try:
                        self.stages.index("Stage Three")
                    except ValueError:
                        self.stages.append("Stage Three")
                    else:
                        pass 
                    break
                elif value == 2:
                    print("You choose 2, you lose.")
                    self.check_life(1)
                    break
                elif value == 3:
                    print("You choose 3, you lose.")
                    self.check_life(1)
                    break

    def Dream_World(self):
        interaction = """
        (The Dream World)
            You are in a dream and you are about to be eating by a Tiger what is the best option to do?
            1. Wake Up
            2. Run
            3. Kil it
        """
        print(interaction)
        while True:
            try:
                option = int(input("What will you do? (eg. 1, 2, 3) "))
            except ValueError:
                print('please enter a number... ')
            else:
                if option == 1:
                    print("""You choose option 1, you win.""")
                    self.money += 500
                    self.gold += 100
                    if self.have_key == 2:
                        self.key += 1
                        self.have_key += 1
                    try:
                        self.stages.index("Stage Four")
                    except ValueError:
                        self.stages.append("Stage Four")
                    else:
                        pass 
                    break
                elif option == 2:
                    print("You choose 2, you lose.")
                    self.check_life(1)
                    break
                elif option == 3:
                    print("You choose 3, you lose.")
                    self.check_life(1)
                    break 

    def River_World(self):
        interaction = """
        (The River World)
            This is the Final Stage of the game, in this section you might have to cross a very big River.
            What is the enjoyable, expensive and most luxurious way to cross?
            1. Ship
            2. Flight
            3. Fly
        """
        print(interaction)
        while True:
            try:
                option = int(input("What will you choose? (eg. 1, 2, 3) "))
            except ValueError:
                print('please enter a number... ')
            else:
                if option == 1:
                    print("""You choose option 1, you win.""")
                    print('Congratulation, You finish the game.')
                    self.money += 500
                    self.gold += 100
                    if self.have_key == 3:
                        self.key += 1
                        self.have_key += 1
                    break
                    
                elif option == 2:
                    print("You choose 2, you lose.")
                    self.check_life(1)
                    break
                elif option == 3:
                    print("You choose 3, you lose.")
                    self.check_life(1)
                    break      

class Map(Interaction):

    def Bar(self):
        self.Barman()
        self.Bar_Game()

    def School(self):
        self.School_Question()

    def Dream(self):
        self.Dream_World()

    def River(self):
        self.River_World()

class Stage(Map):

    def Stage_One(self):
        self.Bar()

    def Stage_Two(self):
        self.School()

    def Stage_Three(self):
        self.Dream()

    def Stage_Four(self):
        self.River()

# Main Game Function
class BORING_SPACE_DRAGON_ADVENTURE(Stage):

    def Info(self):
        info = f"""
        KEYS: {self.key}
        GOLD: {self.gold}
        LIFE: {self.life}
        MONEY: ${self.money}
        """
        print(info)

    def Select_Stage(self):
        
        while True:
            num = 1
            for i in range(0, len(self.stages)):
                print(f'{i + 1} {self.stages[i]}')
                num += 1
            print(f'{num} Exit')
            if self.end_game == True:
                break

            try:
                user_stage_select = input('select eg. (Stage One)... ').title()
            except ValueError:
                print('Invalid command')
            else:
                try:
                    check_stage = self.stages.index(user_stage_select)
                except ValueError:
                    if user_stage_select == 'Exit':
                        self.back = True
                        break
                    else:
                        print('this stage is currently not available')
                else:
                    if check_stage == 0:
                        self.Stage_One()
                        
                    elif check_stage == 1:
                        self.Stage_Two()
                        
                    elif check_stage == 2:
                        self.Stage_Three()
                        
                    elif check_stage == 3:
                        self.Stage_Four()
                        
                


    def begin(self):
        self.back = False
        print()
        print(f'Welcome {self.name}')
        print('Select what you want to do?... ')
        print('1. Start Game')
        print('2. Status')
        print('3. Quit')
        self.check()

    def check(self):
        print()
        while True:
            if self.end_game == True:
                break

            if self.back:
                break

            try:
                user_input = int(input('choose a number from the list listed above... '))
            except ValueError:
                print('please enter a number...')
            else:
                if user_input == 1:
                    print('\nSelect Stage:\n')
                    self.Select_Stage()
                    
                elif user_input == 2:
                    self.Info()
                elif user_input == 3:
                    print('Thank you for playing :)')
                    self.end_game = True
                    break
                else:
                    pass

print_text = """"
##################################################
**************************************************
     WELCOME TO BORING SPACE DRAGON ADVENTURE
**************************************************
##################################################
"""

print(print_text)
names = input('Your Name? ')
Rea = BORING_SPACE_DRAGON_ADVENTURE(names)

while True:
    Rea.begin()
    if Rea.end_game:
        break

    
