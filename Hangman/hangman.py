import random
import string
from words import wlist
def get_word(wlist,difficulty):
    if difficulty=='1':
        word=random.choice(wlist)
        while '-' in word or ' ' in word or len(word)>4:
            word=random.choice(wlist)
        return word
    elif difficulty=='2':
        word=random.choice(wlist)
        while '-' in word or ' ' in word or len(word)>7:
            word=random.choice(wlist)
        return word
    elif difficulty=='3':
        word=random.choice(wlist)
        while '-' in word or ' ' in word or len(word)<7:
            word=random.choice(wlist)
        return word

def logic(choice,difficulty):
    alphabet=set(string.ascii_uppercase)
    used=set()
    if choice=='1':
        file='hobbies.txt'
    elif choice=='2':
        file='countries.txt'
    elif choice=='3':
        file='animals.txt'
    elif choice=='4':
        print('The word is a random noun.')
    else:
        print("Invalid choice.")
        exit(0)
    if choice=='1' or choice=='2' or choice=='3':
        lst=[]
        with open(file) as f:
            lst=[line.rstrip() for line in f]
        word=get_word(lst,difficulty).upper() 
    else:
          word=get_word(wlist,difficulty).upper() 
    letters_in_word=set(word)
    life=len(word)
    turn=1
    while len(letters_in_word)>0 and life!=0: 
        if turn ==1:
            print("Current word:",end=' ')
            for letter in word:
                print('_',end=' ')
            print()
            print('This word belongs to {} and has {} letters. Good luck!'.format(cat(choice),len(word)))
            print()
            ip=input(f'Guess a letter. You have {life} lives.').upper()
        if turn!=1:
            print('You have already used:',','.join(used))  #This concatenates the set used to the string
            ip=input(f'You have {life} lives.').upper()

        if ip in alphabet-used:
            used.add(ip)
            if ip in letters_in_word:
                print(f'{ip} is present in the word!')
                letters_in_word.remove(ip)
            else:
                print(f'Oops!{ip} is not in the word. You lost a life!')
                life-=1
        elif ip in used:
            print(f'Already guessed {ip}. Please try again.')
        else:
            print("Invalid character. Take a guess using alphabets only.")
        word_guessed=[letter if letter in used else '_' for letter in word] 
        print('Current word:',' '.join(word_guessed))   #This concatenates the set word guessed to the string
        turn+=1
        print()
        if life==0:
            print("You died.")
    if life!=0:
        print("Congragulations!! You got the word right!")
    print(f'The word was {word}')
    print()

def cat(choice):
    if choice=='1':
        return 'HOBBIES/ INTERESTS'
    elif choice=='2':
        return 'COUNTRIES'
    elif choice=='3':
        return 'ANIMALS/ BIRDS'
    elif choice=='4':
        return 'RANDOM'

print("Welcome to Hangman.\nRULES:\nYou can choose a category from which you have to guess a word.\nYou get as many lives as the number of the letters in the chosen word.\nThe game ends when you lose all the lives or when you guess the word correctly")
print("Choose a category.")
choice=input("1.Hobbies/Interests 2.Countries 3.Animals/Birds 4.Random\n")
difficulty=input("Choose word length- 1. Word length <=4  2. Word length <=7 3. Word length >7\n")
if int(difficulty)>3 or int(difficulty)<1:
    exit(0)
logic(choice,difficulty)