import random
from SenseCells.tts import tts

def who_are_you():
    messages = ['I am Melissa, your lovely personal assistant.',
        'Melissa, didnt I tell you before?',
        'You ask that so many times! I am Melissa.']
    tts(random.choice(messages))

def how_am_i():
    replies = ['You are goddamn handsom!',
        'My knees goes weak when I see you.',
        'You are sexy!',
        'You look like the kindest person I have met.']
    tts(random.choice(replies))

def tell_joke():
    jokes = ['What happens to a frogs car when it breaks down? It gets toad away',
        'Why was six scared of seven? Because seven ate nine.',
        'No, I always forget the pounch line.']
    tts(random.choice(jokes))

def who_am_i(name):
    tts('You are ' + name + ', a brilliant person. I love you!')

def where_born():
    tts('I was created by a magician named Yogi, in India, the magical land of Himalayas.')

def how_are_you():
    tts('I am fine, thank you.')

def undefined():
    tts('Sorry, I dont know what that means!')
