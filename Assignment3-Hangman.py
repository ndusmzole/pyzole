import random
rep = True
x = "y"
def replay():

    if x == "y":
        repl = True
    else:
        repl = False
def play():
    list1 = "this is my word to test the hangman program".split()

    random.shuffle(list1)
    f = list1[3]
    m = []
    for d in f:
        m.append(d)
    x = "".join(m)
    letter = " "

    word = x
    word1 = word
    guessed = []
    count = 0
    graphics = [
        """
            +--------+
             |
             |
             |
             |
             |
             |
         ====================
        """,
        """
            +-------
            |      o
            |
            |
            |
            |
        ====================
        """,
        """
            +-------
            |      o
            |      +
            |      |
            |
            |
        ======================
        """,
        """
            +-------
            |       o
            |    ---+
            |       |
            |
            |
            |
        =====================
        """,
        """
            +-------
            |       o
            |    ---+---
            |       |
            |
            |
            |
            |
        =====================
        """,
        """
            +-------
            |       o
            |    ---+---
            |       |
            |      /
            |     /
            |    /
            |
        =====================
        """,
        """
            +-------
            |       o
            |    ---+---
            |       |
            |      / \
            |     /   \
            |    /     \
            |
        =====================
        """]

    def livesCount(a):
        if(a == 1):
            print(graphics[1]+"\n")
        elif(a == 2):
            print(graphics[2]+"\n")
        elif(a == 3):
            print(graphics[3]+'\n')
        elif(a == 4):
            print(graphics[4]+"\n")
        elif(a == 5):
            print(graphics[5]+"\n")
        else:
            print(graphics[6]+"\n")

    def dashes(wor):
        temp = wor

        for i in wor:
            temp = temp.replace(i, "-")
        return temp

    def input_letter():
        while True:
            letter = input("Please input a single letter: ")
            return letter

    def listingAndJoin(aword, ind, chara):      #Helper Method
        thelist = list(aword)
        thelist[ind] = chara
        thelist = "".join(thelist)
        return thelist


    wor = dashes(word)
    temp = wor

    while(True):
        letter = input_letter()

        # manual codo
        if letter in guessed and letter not in word1:
            print("You have already guessed the letter.")
            count += 1
            livesCount(count)
        elif letter not in word1:
            print("Your guess is incorrect.")
            count += 1
            livesCount(count)
        else:
            print("You have guessed: %s" % letter)
            print("Your guess was correct")
            guessed.append(letter)
        # manual codo ends
        y = 0
        if count == 6:
            livesCount(count)
            print("Game over Pal!!!")
            break

        for x in word1:
            if letter == x:
                word1 = listingAndJoin(word1, y, "-")   # This here is the updated secret word
                word = listingAndJoin(wor, y, x)       # This is the letters guessed placed at their locating in secret word
                break
            y += 1
            word = wor
        if word1 == temp:
            print("*** You Won ***\n*** The secret word is: %s ***" % word)
            print("*** Your Number Of Wrong Guesses: %d ***" % count)
            break
        print("word: "+word)
        wor = word

while rep:
     play()
     x = input("Wanna play again? yes press <<y>> no press <<n>>")
     if x == "y":
         rep = True
     else:
         break



















